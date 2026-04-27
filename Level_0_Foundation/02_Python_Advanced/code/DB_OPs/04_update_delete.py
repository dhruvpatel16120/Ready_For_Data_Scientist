import sqlite3

DB_PATH = "Level_0_Foundation/02_Python_Advanced/code/DB_OPs/example.db"

def modify_data():
    print("--- SQLite: Update and Delete Operations ---")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # 1. Update Data
    new_age = 26
    target_email = "alice@example.com"
    cursor.execute("UPDATE users SET age = ? WHERE email = ?", (new_age, target_email))
    print(f"Updated age for {target_email} to {new_age}. Rows affected: {cursor.rowcount}")

    # 2. Delete Data
    delete_target = "charlie@example.com"
    cursor.execute("DELETE FROM users WHERE email = ?", (delete_target,))
    print(f"Deleted user with email {delete_target}. Rows affected: {cursor.rowcount}")

    conn.commit()
    conn.close()
    print("Modification operations completed.\n")

if __name__ == "__main__":
    modify_data()
