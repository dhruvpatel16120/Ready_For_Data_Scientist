import sqlite3
import time

DB_PATH = "Level_0_Foundation/02_Python_Advanced/code/DB_OPs/example.db"

def performance_demo():
    print("--- SQLite: Indexes and Performance ---")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Searching WITHOUT an index
    print("Searching for a specific user WITHOUT an index...")
    start_time = time.time()
    for _ in range(1000):
        cursor.execute("SELECT * FROM users WHERE email = ?", ("alice@example.com",))
    print(f"1000 searches took: {time.time() - start_time:.4f} seconds")

    # 2. Creating an Index
    print("\nCreating index on 'email' column...")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_user_email ON users(email)")
    
    # 3. Searching WITH an index
    print("Searching WITH an index...")
    start_time = time.time()
    for _ in range(1000):
        cursor.execute("SELECT * FROM users WHERE email = ?", ("alice@example.com",))
    print(f"1000 searches took: {time.time() - start_time:.4f} seconds")

    # 4. Using EXPLAIN QUERY PLAN
    print("\nExplaining the query plan:")
    plan = cursor.execute("EXPLAIN QUERY PLAN SELECT * FROM users WHERE email = ?", ("alice@example.com",)).fetchone()
    print(f"Plan: {plan[3]}")

    conn.close()
    print("\nPerformance demo completed.\n")

if __name__ == "__main__":
    performance_demo()
