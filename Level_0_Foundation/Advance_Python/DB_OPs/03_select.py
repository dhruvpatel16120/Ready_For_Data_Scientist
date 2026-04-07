import sqlite3

DB_PATH = "example.db"

def query_data():
    print("--- SQLite: Querying Data ---")
    conn = sqlite3.connect(DB_PATH)
    
    # Optional: Set the row_factory to sqlite3.Row to access columns by name
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # 1. Fetching All Records
    print("Fetching all users:")
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()  # Returns a list of all matching rows
    
    for row in rows:
        # Accessing by column name because we used row_factory
        print(f"ID: {row['id']} | Name: {row['name']} | Email: {row['email']} | Age: {row['age']}")

    # 2. Fetching a Single Record
    print("\nFetching specific user (Age > 25):")
    cursor.execute("SELECT name, email FROM users WHERE age > ?", (25,))
    row = cursor.fetchone()
    if row:
        print(f"First match: {row['name']} ({row['email']})")

    # 3. Using cursors as iterators (Memory efficient for large datasets)
    print("\nIterating over results directly:")
    for row in cursor.execute("SELECT name FROM users ORDER BY age DESC"):
        print(row['name'])

    conn.close()
    print("Query operations completed.\n")

if __name__ == "__main__":
    query_data()
