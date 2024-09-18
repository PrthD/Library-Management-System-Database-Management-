
# Library-Management-System (Database-Management)

## Project Overview
This Library Management System is a database-driven project designed to manage a library's users, books, and penalties. The system allows users to register, log in, search for books, borrow and return books, view their profile, and manage any penalties associated with overdue books. The system is built using Python and SQLite.

## Code Execution Guide

### Files Needed for Execution
- **`dbSetup.py`**: Initializes the database using the provided schema.
- **`userManagement.py`**: Handles user-related functionalities such as registration and login.
- **`penaltyManagement.py`**: Manages penalty-related functionalities, including viewing and paying penalties.
- **`bookManagement.py`**: Manages book-related functionalities, such as searching, borrowing, and returning books.
- **`utils.py`**: Contains utility functions used throughout the project, including user input prompts.
- **`main.py`**: The main driver script that serves as the user interface for interacting with the system.
- **`mp1-schema.sql.txt`**: An SQL schema file containing the necessary commands to create database tables.
- **`test.db`**: A pre-populated SQLite database file used for testing and demonstration purposes.

### How to Execute the Program
1. Ensure you have **Python 3** installed. You can verify by running:
   ```bash
   python3 --version
   ```
2. Place all the files mentioned above in the same directory.
3. Open a terminal or command prompt, and navigate to the directory containing your project files.
4. Execute the program by running the following command:
   ```bash
   python3 main.py mp1-schema.sql.txt test.db
   ```

## Navigating the Program
Once the program is running, you'll be presented with the main menu of the Library Management System. Below are the available options and how to use them:

### Main Menu Options:
- **Login**: If you're an existing user, select this option to log in by providing your email and password.
- **Register**: New users can create an account by entering details like email, password, name, birth year (optional), and faculty (optional).
- **Exit**: Select this option to exit the program.

### After Logging In:
Once logged in, you’ll see additional options in the user menu:

- **View Profile**: Displays your user profile, including details like name, email, birth year, faculty, and borrowing and penalty history.
- **Search for Books**: Allows you to search for books by keywords. You can view book details and check the availability for borrowing.
- **Borrow a Book**: Borrow a book by entering its book ID, provided it is available.
- **Return a Book**: View your currently borrowed books and return any book. If a book is overdue, the system will apply penalties.
- **Pay a Penalty**: View outstanding penalties and make payments either partially or in full.
- **Logout**: Logs you out and returns you to the main menu.

### Input Validation:
The system provides input validation to ensure smooth interaction, guiding you through correct usage and preventing common input errors.

### Enjoy Managing Your Library!
