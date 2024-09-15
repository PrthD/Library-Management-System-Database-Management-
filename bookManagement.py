"""
Implementation of Book Management
Purpose: Handles book-related operations, such as searching for books, borrowing, returning, and reviewing books. 
         It interact with the books, borrowings, and reviews tables.
"""
from datetime import datetime, timedelta

class BookManagement:
    def __init__(self, conn) -> None:
        self.conn = conn
    
    def searchBooks(self, keyword, userId) -> None:
        """
        Purpose: Searches for books that match the given keyword and displays them 5 per page.
                After displaying, allows users to choose a book ID to borrow.
        Parameter: keyword: string, 
                   userId: string
        Returns: None
        """
        page = 1
        while True:
            offset = (page - 1) * 5  # Calculate offset for pagination
            keyword_pattern = f'%{keyword}%'  # Prepare keyword for LIKE query

            query = """
                SELECT bk.book_id, bk.title, bk.author, bk.pyear, 
                    IFNULL(AVG(rev.rating), 'No Ratings') AS avg_rating,
                    CASE WHEN COUNT(bor.book_id) > 0 THEN 'Unavailable' ELSE 'Available' END AS availability
                FROM books bk
                LEFT JOIN reviews rev ON bk.book_id = rev.book_id
                LEFT JOIN borrowings bor ON bk.book_id = bor.book_id AND bor.end_date IS NULL
                WHERE bk.title LIKE ? OR bk.author LIKE ?
                GROUP BY bk.book_id, bk.title, bk.author, bk.pyear
                ORDER BY 
                    CASE WHEN bk.title LIKE ? THEN 1 ELSE 2 END, 
                    CASE WHEN bk.title LIKE ? THEN bk.title ELSE bk.author END
                LIMIT 5 OFFSET ?
            """

            cursor = self.conn.cursor()
            cursor.execute(query, (keyword_pattern, keyword_pattern, keyword_pattern, keyword_pattern, offset))
            books = cursor.fetchall()

            if books:
                for book in books:
                    print(f"Book ID: {book[0]}, Title: '{book[1]}', Author: '{book[2]}', Publish Year: {book[3]}, Average Rating: {book[4]}, Availability: {book[5]}")
            
                borrow_choice = input("\nEnter a Book ID to borrow or type 'n' to continue browsing: ").lower()
                if borrow_choice.isdigit():
                    self.borrowBook(userId, borrow_choice)
                elif borrow_choice == 'n':
                    more_books = input("View next page? (y/n): ").lower()
                    if more_books == 'y':
                        page += 1  # Move to the next page
                    else:
                        break  # Exit search if the user doesn't want to view more books
                else:
                    print("Invalid input. Please enter a valid Book ID or 'n' to continue.")
            else:
                if page == 1:
                    print("No matching books found.")
                else:
                    print("No more books.")
                break
    
    def borrowBook(self, userId, bookId) -> None:
        """
        Purpose: Borrows a book with the given book ID
        Parameter: userId: string,
                   bookId: string
        Returns: None
        """
        cursor = self.conn.cursor()

        # First, check if the book exists in the database
        cursor.execute("SELECT * FROM books WHERE book_id = ?;", (bookId,))
        if not cursor.fetchone():
            print(f"No book found with Book ID {bookId}.")
            return

        # Check if the book is already borrowed
        cursor.execute("SELECT * FROM borrowings WHERE book_id = ? AND end_date IS NULL;", (bookId,))
        if cursor.fetchone():
            print("The book is already borrowed.")
            return

        # bid = int(datetime.datetime.now().timestamp())
        start_date = datetime.now().strftime("%Y-%m-%d")

        cursor.execute("INSERT INTO borrowings (member, book_id, start_date) VALUES (?, ?, ?);", (userId, bookId, start_date))
        self.conn.commit()
        print(f"Book with Book ID {bookId} borrowed successfully.")

    def returnBook(self, userId) -> None:
        """
        Purpose: Mark a book as returned, apply penalties if overdue, display current borrowings,
                and optionally add a book review.
        Parameter: userId: string
        Returns: None
        """
        cursor = self.conn.cursor()

        # Display current borrowings
        cursor.execute('''SELECT b.bid, bk.title, b.start_date
                          FROM borrowings b
                          JOIN books bk ON b.book_id = bk.book_id
                          WHERE b.member=? AND b.end_date IS NULL''', (userId,))
        borrowings = cursor.fetchall()
        
        # Check if the user has current borrowings
        if not borrowings:
            print("No current borrowings.")
            return
        
        # Display current borrowings to the user
        print("\nCurrent Borrowings:")
        for bid, title, start_date in borrowings:
            return_deadline = datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=20)
            print(f"Borrowing ID: {bid}, Title: '{title}', Borrowing Date: {start_date}, Return Deadline: {return_deadline.date()}")

        # Prompt user to enter a borrowing ID to return
        borrowingId = input("\nEnter borrowing ID to return a book or type 'exit' to return to Menu: ")
        if borrowingId.lower() == 'exit':
            return  # User chose to exit

        # Get borrowing details
        cursor.execute('SELECT book_id, start_date FROM borrowings WHERE bid=? AND member=? AND end_date IS NULL', (borrowingId, userId))
        borrowing = cursor.fetchone()
        if not borrowing:
            print("Borrowing record not found or book already returned.")
            return

        book_id, start_date = borrowing
        return_date = datetime.now().date()
        start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
        overdue_days = (return_date - start_date).days - 20

        # Update the borrowings table with the return date
        cursor.execute('UPDATE borrowings SET end_date=? WHERE bid=?', (return_date, borrowingId))

        # Apply penalty if overdue
        if overdue_days > 0:
            penalty_amount = overdue_days
            cursor.execute('INSERT INTO penalties (bid, amount, paid_amount) VALUES (?, ?, NULL)', (borrowingId, penalty_amount))
            print(f"Book returned late. A penalty of ${penalty_amount} has been applied.")

        # Handle book review
        review_choice = input("\nWould you like to leave a review for this book? (y/n): ").lower()
        if review_choice == 'y':
            while True:
                try:
                    rating = float(input("Rating (1-5): "))
                    if 1 <= rating <= 5:
                        break
                    else:
                        print("Rating must be between 1 and 5.")
                except ValueError:
                    print("Invalid input. Please enter a rating between 1 and 5.")
            
            review_text = input("Review: ")
            review_date = return_date
            cursor.execute('INSERT INTO reviews (book_id, member, rating, rtext, rdate) VALUES (?, ?, ?, ?, ?)', 
                           (book_id, userId, rating, review_text, review_date))
            print("Thank you for your review!")

        self.conn.commit()