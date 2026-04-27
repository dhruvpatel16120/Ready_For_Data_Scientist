# 🗄️ SQLite Masterclass: Python Database Operations

Welcome to the **Database Operations (DB_OPs)** module. This directory provides a hands-on, step-by-step journey into managing relational data using Python's built-in `sqlite3` library. From basic CRUD operations to advanced performance tuning and custom SQL extensions, this module covers everything a Data Scientist needs to handle local data efficiently.

---

## 🗺️ Learning Roadmap

This module is structured as a progressive curriculum. Each file builds upon the previous one:

### 1️⃣ The Fundamentals
| File | Topic | Key Learning Objective |
| :--- | :--- | :--- |
| `01_basics.py` | **Connections & Tables** | Establishing connections and defining schema with data types. |
| `02_insert.py` | **Data Ingestion** | Bulk inserts and protecting against SQL Injection using parameters. |
| `03_select.py` | **Querying Data** | Fetching results and using `Row` factories for cleaner data access. |
| `04_update_delete.py` | **Modifying Data** | Safely updating existing records and handling deletions. |

### 2️⃣ Advanced Database Control
| File | Topic | Key Learning Objective |
| :--- | :--- | :--- |
| `05_advanced.py` | **Transactions** | ACID compliance, manual commit/rollback, and context managers. |
| `06_relationships.py` | **Joins & FKs** | Managing relational data and enforcing integrity with Foreign Keys. |
| `07_performance_indices.py` | **Indexing** | Speeding up lookups with `CREATE INDEX` and `EXPLAIN QUERY PLAN`. |

### 3️⃣ Integration & Extensions
| File | Topic | Key Learning Objective |
| :--- | :--- | :--- |
| `08_export_data.py` | **Data Portability** | Exporting SQL results directly to CSV and JSON formats. |
| `09_custom_extensions.py` | **Power User Tools** | In-Memory DBs and custom Python-powered SQL functions. |

---

## 🚀 Key Concepts Covered

### 🛡️ Security First: Parameterized Queries
Never use f-strings or `.format()` to build SQL queries. This module teaches you the "Pythonic" way to pass parameters:
```python
# GOOD
cursor.execute("SELECT * FROM users WHERE email = ?", (user_email,))

# BAD (SQL Injection Risk)
cursor.execute(f"SELECT * FROM users WHERE email = '{user_email}'")
```

### ⚡ Performance Optimization
Learn why `CREATE INDEX` is your best friend when dealing with large datasets. We demonstrate 10x+ speed improvements and how to peek under the hood with `EXPLAIN QUERY PLAN`.

### 🧪 In-Memory Databases
Perfect for unit tests and temporary data processing. Use `:memory:` to create a lightning-fast database that vanishes when the script ends.

---

## 🛠️ Setup & Usage

1. **Environment**: No external libraries required! Python comes with `sqlite3` built-in.
2. **Running**: Execute the scripts in numerical order to see the database evolve.
   ```bash
   python 01_basics.py
   python 02_insert.py
   ...
   ```
3. **Database File**: Most scripts will interact with `example.db`. You can view this file using tools like [DB Browser for SQLite](https://sqlitebrowser.org/).

---

> [!TIP]
> **Pro Tip**: Always enable foreign key support manually in SQLite using `PRAGMA foreign_keys = ON;`, as it is disabled by default for backward compatibility!

---
*Created as part of the "Zero to Data Scientist" Foundation Series.*
