import sqlite3
import os

# Define the database path
DB_PATH = "example.db"

def basic_operations():
    print("--- SQLite Basics: Connection & Table Creation ---")
    
    # 1. Connect to the database (creates the file if it doesn't exist)
    # The connection object represents the database
    conn = sqlite3.connect(DB_PATH)
    
    # 2. Create a cursor object
    # The cursor allows us to execute SQL commands
    cursor = conn.cursor()
    
    # 3. Create a table
    # Standard SQL syntax works here
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            age INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    print("Table 'users' created successfully.")
    
    # 4. Commit the changes
    conn.commit()
    
    # 5. Close the connection
    conn.close()
    print("Connection closed.\n")

if __name__ == "__main__":
    basic_operations()
