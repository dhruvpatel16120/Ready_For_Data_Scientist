import sqlite3

DB_PATH = "example.db"

def insert_data():
    print("--- SQLite: Inserting Data ---")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Insert a single record using parameterized query (prevents SQL injection)
    # Never use f-strings for SQL queries!
    user_data = ("Alice Smith", "alice@example.com", 25)
    cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", user_data)
    print(f"Inserted single user: {user_data[0]}")

    # 2. Insert multiple records (Bulk Insert)
    users_list = [
        ("Bob Johnson", "bob@example.com", 30),
        ("Charlie Brown", "charlie@example.com", 22),
        ("David Wilson", "david@example.com", 35),
        ("Eve Davis", "eve@example.com", 28)
    ]
    
    # executemany is much faster for bulk data
    try:
        cursor.executemany("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", users_list)
        print(f"Inserted {len(users_list)} users in bulk.")
    except sqlite3.IntegrityError:
        print("Note: Some users might already exist (Unique Email constraint).")

    conn.commit()
    conn.close()
    print("Insert operations completed.\n")

if __name__ == "__main__":
    insert_data()
