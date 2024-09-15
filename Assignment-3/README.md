# Code execution guide
> Files Needed for the execution of program:
1. dbSetup.py: Initializes the database using the provided schema.
2. userManagement.py: Handles user-related functionalities like registration and login.
3. penaltyManagement.py: Manages penalty-related functionalities, such as viewing and paying penalties.
4. bookManagement.py: Manages book-related functionalities, including searching, borrowing, and returning books.
5. utils.py: Contains utility functions used across the project, such as prompts for user input.
6. main.py: The main driver script that provides the user interface for interacting with the system.
7. mp1-schema.sql.txt: The SQL schema file containing the commands to create the necessary database tables.
8. test.db: An SQLite database file used for testing, pre-populated with some data for demonstration purposes.

> How to Execute the Program:
1. Ensure you have Python 3 installed on your system. You can check by running "python3 --version" in your terminal.
2. Place all the above-mentioned files in the same directory.
3. Open a terminal or command prompt and navigate to the directory containing your files.
4. Execute the program by running the following command: "python3 main.py mp1-schema.sql.txt test.db"

> Navigating the Program:
Once the program is running, you will be greeted with the main menu of the Library Management System. Here are the options you will see and how to use them:
1. Login: If you're an existing user, choose this option to log in. You'll be prompted to enter your email and password.
2. Register: New users should select this option to create an account. You'll need to provide an email, password, name, optional birth year, and optional faculty name.
4. Exit: Choose this option to quit the program.

> After logging in, you will be presented with the user menu:
1. View Profile: Displays your user profile, including your name, email, birth year, faculty, and borrowing and penalty history.
2. Search for Books: Allows you to search for books by keyword. You can view book details and choose to borrow an available book.
3. Borrow a Book: Directly borrow a book by entering its book ID. You'll only be allowed to borrow if the book is available.
4. Return a Book: View your current borrowings and select a book to return. Overdue books will incur penalties.
5. Pay a Penalty: View outstanding penalties and choose to pay them either in full or partially.
6. Logout: Logs you out of the system and returns you to the main menu.

Follow the on-screen prompts to navigate through the system. Input validation is provided for operations to guide you through the correct usage and to prevent common input errors.

Enjoy managing your library!
