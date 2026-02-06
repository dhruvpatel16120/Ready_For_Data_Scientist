# SQLite in Python: From Zero to Hero

This folder contains a comprehensive guide to using SQLite with Python's built-in `sqlite3` module.

## Files Overview

1. **`01_basics.py`**: Covers connecting to a database and creating tables with appropriate data types.
2. **`02_insert.py`**: demonstrates how to insert data securely using parameterized queries to prevent SQL injection. Shows both single and bulk inserts (`executemany`).
3. **`03_select.py`**: Shows how to retrieve data using `fetchone`, `fetchall`, and row factories for named column access.
4. **`04_update_delete.py`**: Explains how to modify existing records and safely delete them.
5. **`05_advanced.py`**: Dives into transactions, manual rollbacks, and writing custom context managers for database operations.

## Key Points
- **Security**: Always use `?` placeholders instead of string formatting for queries.
- **Persistence**: Don't forget to call `conn.commit()` after write operations (INSERT, UPDATE, DELETE).
- **Resources**: Always close your connection with `conn.close()` or use context managers.
