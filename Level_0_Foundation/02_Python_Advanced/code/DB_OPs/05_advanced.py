import sqlite3
from contextlib import contextmanager

DB_PATH = "Level_0_Foundation/02_Python_Advanced/code/DB_OPs/example.db"

@contextmanager
def db_transaction():
    """Context manager for handling transactions automatically."""
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Transaction failed, rolling back: {e}")
        raise
    finally:
        conn.close()

def advanced_operations():
    print("--- SQLite Advanced: Transactions & Context Managers ---")
    
    # Using 'with' manual connection (Python's sqlite3 connection can be used as CM)
    # Note: connect() as a CM only commits/rolls back, it doesn't close the connection automatically.
    
    print("\n1. Using custom transaction context manager:")
    try:
        with db_transaction() as conn:
            cursor = conn.cursor()
            # This query is fine
            cursor.execute("UPDATE users SET age = age + 1")
            print("Successfully incremented age for all users.")
            
            # Uncomment below to trigger a rollback
            # cursor.execute("INSERT INTO non_existent_table (test) VALUES ('fail')")
    except Exception:
        pass

    # 2. Aggregates and JSON (SQLite supports JSON functions)
    print("\n2. Aggregate functions:")
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT AVG(age), MAX(age), COUNT(*) FROM users")
        avg_age, max_age, total = cursor.fetchone()
        print(f"Average Age: {avg_age if avg_age else 0:.1f}")
        print(f"Max Age: {max_age}")
        print(f"Total Users: {total}")

    print("\nAdvanced operations completed.\n")

if __name__ == "__main__":
    advanced_operations()
