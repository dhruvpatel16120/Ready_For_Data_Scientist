import sqlite3

DB_PATH = "example.db"

def relational_demo():
    print("--- SQLite: Joins and Relationships ---")
    conn = sqlite3.connect(DB_PATH)
    # Enable foreign key support (disabled by default in SQLite for backwards compatibility)
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    # 1. Create a related table (Posts belonging to Users)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            title TEXT NOT NULL,
            content TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        )
    ''')

    # 2. Insert some related data
    # Let's get Alice's ID first
    cursor.execute("SELECT id FROM users WHERE email = ?", ("alice@example.com",))
    user_id = cursor.fetchone()[0]

    posts = [
        (user_id, "Hello World", "This is my first post!"),
        (user_id, "Python is Great", "SQLite makes it easy to store data.")
    ]
    cursor.executemany("INSERT INTO posts (user_id, title, content) VALUES (?, ?, ?)", posts)
    print(f"Inserted {len(posts)} posts for user ID {user_id}")

    # 3. Perform a JOIN query
    print("\nFetching posts with user names (INNER JOIN):")
    query = '''
        SELECT users.name, posts.title 
        FROM users 
        INNER JOIN posts ON users.id = posts.user_id
    '''
    for row in cursor.execute(query):
        print(f"User: {row[0]} | Post Title: {row[1]}")

    conn.commit()
    conn.close()
    print("\nRelational operations completed.\n")

if __name__ == "__main__":
    relational_demo()
