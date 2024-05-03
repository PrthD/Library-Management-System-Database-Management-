import sys
import sqlite3
from userManagement import UserManagement
from bookManagement import BookManagement
from penaltyManagement import PenaltyManagement
from dbSetup import initializeDatabase
from utils import *

def userMenu(userMgr, bookMgr, penaltyMgr, userId):
    """
    Purpose: Displays the main user menu and handles user interactions for various functionalities like viewing the profile,
             searching for books, borrowing and returning books, and managing penalties.

    Parameters:
    - userMgr (UserManagement): An instance of UserManagement to handle user-related functionalities.
    - bookMgr (BookManagement): An instance of BookManagement to handle book-related functionalities.
    - penaltyMgr (PenaltyManagement): An instance of PenaltyManagement to handle penalty-related functionalities.
    - userId (str): The unique identifier of the currently logged-in user.

    Returns: None
    """
    while True:
        print("\n--- User Menu ---")
        print("1. View Profile")
        print("2. Search for Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Pay a Penalty")
        print("6. Logout")
        userChoice = input("Enter choice: ")

        if userChoice == '1':
            userMgr.viewProfile(userId)
        elif userChoice == '2':
            keyword = input("\nEnter search keyword or type '*' to return to Menu: ")
            if keyword != '*':
                bookMgr.searchBooks(keyword, userId)
        elif userChoice == '3':
            bookId = input("\nEnter book ID to borrow or type 'exit' to return to Menu: ")
            if bookId.lower() != 'exit':
                bookMgr.borrowBook(userId, bookId)
        elif userChoice == '4':
            bookMgr.returnBook(userId)
        elif userChoice == '5':
           penaltyMgr.managePenalties(userId)
        elif userChoice == '6':
            break  # Logs the user out by breaking out of the loop
        else:
            print("Invalid choice.")


def main(schemaFile, dataFile):
    dbFileName = "database.db"
    conn = sqlite3.connect(dbFileName)
    print(f"Connected to database: {dbFileName}")

    # Initialize the database using schema and populate it with initial data
    initializeDatabase(conn, schemaFile, dataFile)

    # Initialize modules
    userMgr = UserManagement(conn)
    bookMgr = BookManagement(conn)
    penaltyMgr = PenaltyManagement(conn)

    while True:
        print("\n--- Library Management System ---")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Enter choice: ")
        print("\n")
        
        if choice == '1':    
            email = promptForEmail("Email: ")
            password = promptForNonEmptyPassword("Password: ")
            if userMgr.loginUser(email, password):
                userId = email
                userMenu(userMgr, bookMgr, penaltyMgr, userId)
            else:  # Login failed
                print("Login failed. Invalid email and/or password.")

        elif choice == '2':
            email = promptForEmail("Email: ")
            password = promptForNonEmptyPassword("Password: ")
            name = promptForNonEmptyName("Name: ")
            byear = promptForOptionalBirthYear("Birth Year: ")
            faculty = promptForOptionalFaculty("Faculty: ")
            if userMgr.registerUser(email, password, name, byear, faculty):
                userId = email
                print("Registration successful. You are now logged in.")
                userMenu(userMgr, bookMgr, penaltyMgr, userId)
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice.")

    conn.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <schemaFile> <dataFile>")
        sys.exit(1)

    schemaFile = sys.argv[1]
    dataFile = sys.argv[2]
    main(schemaFile, dataFile)