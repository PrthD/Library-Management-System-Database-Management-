"""
Implementation of User Management
Purpose: Manages user-related functionalities, including registration, login, and viewing member profiles.
         It interacts with the members table in our database.
"""

class UserManagement:
    def __init__(self, conn) -> None:
        self.conn = conn
    
    def loginUser(self, email, password) -> bool:
        """
        Purpose: Attempts to login with the provided info
        Parameter: email: string,
                   password: string
        Returns: True if login was successful
                 False if login failed
        """
        cursor = self.conn.cursor()
        emailLower = email.lower()
        email_password = (emailLower, password)
        cursor.execute('SELECT email FROM members WHERE email=? AND passwd=?;', email_password)
        res = cursor.fetchone()
        if (res is None):  # email and passwd wrong or doesn't exist
            return False
        else:  # successful login
            return True 

    def registerUser(self, email, password, name, byear, faculty) -> bool:
        """
        Purpose: Register an user with provided info
        Parameter: email: string,
                   password: string,
                   name: string,
                   byear: string (OPTIONAL)
                   faculty: string (OPTIONAL)
        Returns: True if registration was successful
                 False if registration failed
        """
        cursor = self.conn.cursor()
        emailLower = email.lower()
        email_tuple = (emailLower, )
        cursor.execute('SELECT email FROM members WHERE LOWER(email)=?;', email_tuple)
        selected = cursor.fetchone()
        if (selected is None):  # email is unique => new account can be registered
            data = (emailLower, password, name, byear, faculty)
            cursor.execute('INSERT INTO members (email, passwd, name, byear, faculty) VALUES (?, ?, ?, ?, ?);', data)
            self.conn.commit()
            return True
        else:  # email not unique
            print("This email has already been registered.")
            return False
    
    def viewProfile(self, email) -> None:
        """
        Purpose: View the logged in user profile using their email
        Parameter: email: string
        Returns: None
        """
        cursor = self.conn.cursor()
        # Query for basic info: name, email, byear
        emailLower = email.lower()
        email_tuple = (emailLower, )
        cursor.execute('SELECT name, email, byear, faculty FROM members WHERE email=?;', email_tuple)
        basic_info = cursor.fetchone()
        name = basic_info[0]
        email = basic_info[1]
        byear = basic_info[2]
        faculty = basic_info[3]
        # Query for all borrowings made
        cursor.execute('SELECT bid, start_date, end_date FROM borrowings WHERE member=?;', email_tuple)
        borrowings_list = cursor.fetchall()
        # Count for previous, current, overdue borrowings
        previous_count = 0
        current_count = 0
        overdue_count = 0
        for b in borrowings_list:
            if b[2] is not None:  # end_date is not NULL => borrowed and returned
                previous_count += 1
            else:  # end_date is NULL => haven't returned -> increment current borrowings and check for overdue
                current_count += 1
                bid = (b[0],)
                cursor.execute("SELECT julianday('now') - julianday(borrowings.start_date) FROM borrowings WHERE bid=?;", bid)
                days_borrowed = cursor.fetchone()[0]
                if days_borrowed > 20:  # more than 20 days borrowed and not returned
                    overdue_count += 1
        # Query for penalties by user
        cursor.execute("SELECT penalties.pid, penalties.amount, penalties.paid_amount FROM borrowings, penalties WHERE borrowings.bid = penalties.bid AND borrowings.member=?;", email_tuple)
        penalties_list = cursor.fetchall()
        # Total debt amount + penalties not paid
        penalties_not_paid = 0
        total_debt = 0
        for p in penalties_list:  # p[1] = amount, p[2] = paid_amount
            if p[2] is None or p[2] < p[1]:  # Penalties not paid in full
                penalties_not_paid += 1
            # Debt calculation
            if p[2] is None:
                total_debt += p[1]
            elif p[2] < p[1]:
                total_debt += (p[1] - p[2])

        # Display profile
        print("\nProfile Page:")
        print("--------------------")
        print(f"Name: {name}")
        print(f"Email: {email}")
        if byear:
            print(f"Birth Year: {byear}")
        if faculty:
            print(f"Faculty: {faculty}")
        print("--------------------")
        print(f"Previous borrowings count: {previous_count}")
        print(f"Current borrowings count: {current_count}")
        print(f"Overdue borrowings count: {overdue_count}")
        print("--------------------")
        print(f"Unpaid penalties count: {penalties_not_paid}")
        print(f"Total debt amount: {total_debt}")
        print("--------------------")
        
        return