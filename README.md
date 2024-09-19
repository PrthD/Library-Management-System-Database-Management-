# Library Management System (Database Management)

## Project Overview
The **Library Management System** is a Python-based project designed to manage a library's operations, including user management, book management, and penalty management. The system uses SQLite for persistent data storage and provides a user-friendly interface for both users and administrators.

## Features

- **User Management**: Allows users to register, log in, and view their profiles.
- **Book Management**: Users can search, borrow, return books, and leave reviews.
- **Penalty Management**: Tracks penalties for overdue books and allows users to pay fines.
- **SQLite Integration**: All data is stored in an SQLite database, managed seamlessly by the system.

## Project Structure

/ (Root directory)
│
├── src/                      # Source code directory
│   ├── main.py               # Main entry point of the application
│   ├── bookManagement.py     # Book management module
│   ├── penaltyManagement.py  # Penalty management module
│   ├── userManagement.py     # User management module
│   ├── utils.py              # Utility functions used across the project
│   └── dbSetup.py            # Database setup and initialization
│
├── sql/                      # Directory for SQL-related files
│   └── mp1-schema.sql.txt    # SQL schema for the database
│
├── data/                     # Data directory
│   └── test.db               # SQLite database file
│
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies (optional)

## Requirements

- **Python 3.x**
- **SQLite** (No external dependencies required)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Library-Management-System-Database-Management.git
   cd Library-Management-System-Database-Management
2. **Navigate to the src/ directory**:
   ```bash
   cd Library-Management-System-Database-Management/src
3. **Run the main application: The main.py script will handle database initialization automatically using the schema and data files. Execute the following command**:
   ```bash
   python3 main.py ../sql/mp1-schema.sql.txt ../data/test.db
   ```
   This command will launch the Library Management System's user interface.

## Usage

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

## Database Schema
The database schema is defined in sql/mp1-schema.sql.txt. It contains the following tables:

- **Members**: Stores user information (email, password, name, birth year, and faculty).
- **Books**: Stores book details (book ID, title, author, and publication year).
- **Borrowings**: Tracks book borrowing activity (book ID, start and end dates).
- **Penalties**: Tracks penalties for overdue book returns.
- **Reviews**: Stores user-submitted book reviews and ratings.
