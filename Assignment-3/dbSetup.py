"""
Implementation of Database Setup
Purpose: Initializes the SQLite database using the provided schema file.
         This script reads the SQL file and executes the commands to create the necessary tables.
"""

import sqlite3

def initializeDatabase(conn, schemaFile, dataFile):
    """
    Purpose: Initializes the database with the provided schema and data files.
             This function reads SQL commands from the schema file to set up the database structure
             and then reads SQL commands from the data file to populate the database with initial data.
    Parameters:
        conn: sqlite3.Connection, the active database connection.
        schemaFile: str, the path to the schema file containing SQL commands for setting up the database structure.
        dataFile: str, the path to the data file containing SQL commands for populating the database with initial data.
    Returns: None
    """
    cursor = conn.cursor()

    # Read and execute the schema SQL commands
    with open(schemaFile, 'r') as f:
        schemaSql = f.read()
    cursor.executescript(schemaSql)

    # Read and execute the data insertion SQL commands
    with open(dataFile, 'r') as f:
        dataSql = f.read()
    cursor.executescript(dataSql)

    # Commit changes
    conn.commit()
    print(f"Database initialized successfully using schema from '{schemaFile}' and data from '{dataFile}'.")