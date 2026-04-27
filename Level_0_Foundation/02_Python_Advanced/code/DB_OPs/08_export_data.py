import sqlite3
import csv
import json

DB_PATH = "Level_0_Foundation/02_Python_Advanced/code/DB_OPs/example.db"

def exporting_demo():
    print("--- SQLite: Data Export (CSV & JSON) ---")
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Fetch all data
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    # 1. Exporting to CSV
    csv_file = "users_export.csv"
    with open(csv_file, "w", newline='') as f:
        writer = csv.writer(f)
        # Write headers
        writer.writerow(users[0].keys())
        # Write data
        for user in users:
            writer.writerow(list(user))
    print(f"Exported users to {csv_file}")

    # 2. Exporting to JSON
    json_file = "users_export.json"
    # Convert Row objects to dictionaries
    users_list = [dict(row) for row in users]
    with open(json_file, "w") as f:
        json.dump(users_list, f, indent=4)
    print(f"Exported users to {json_file}")

    conn.close()
    print("\nExport demo completed.\n")

if __name__ == "__main__":
    exporting_demo()
