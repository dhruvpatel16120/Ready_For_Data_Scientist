# 🐍 Advance Python Mastery

Welcome to the **Advance Python** repository! This project is a comprehensive collection of advanced Python concepts, standard library demonstrations, database operations, and industry best practices. Whether you're mastering Object-Oriented Programming or diving deep into asynchronous I/O, this repository serves as a complete "Zero to Hero" guide.

---

## 📂 Project Structure

The project is organized into focused modules, each covering a specific domain of advanced Python development:

### 📑 1. Core Advanced Concepts
*   **[OOPS](./oops/)**: Mastering Object-Oriented Programming.
    *   Classes, Objects, Constructors, Methods.
    *   Encapsulation, Inheritance, Polymorphism, Abstraction.
    *   Magic Methods (`__str__`, `__repr__`, etc.) and internal relationships.
*   **[Exception Handling](./exception_handling/)**: Building robust and crash-proof applications.
    *   Try, Except, Else, Finally blocks.
    *   Custom exception creation and Python Exception Hierarchy.
*   **[File Handling](./file_handling/)**: Working with various data persistence formats.
    *   Text, CSV, JSON, XML, and Binary files.
    *   Context managers (`with` statement) for safe I/O.
*   **[Modules & Packages](./modules/)**: Mastering code organization.
    *   Built-in vs User-defined modules.
    *   Package design with [Sub-packages](./packages/) like `ecommerce` and `swg_game`.

### 🛠️ 2. The Python Library Suite
*   **[Standard Library Demos](./library/)**: A deep dive into 30+ built-in modules.
    *   **Data & Math**: `math`, `statistics`, `random`, `itertools`, `collections`, `heapq`.
    *   **OS & System**: `os`, `sys`, `pathlib`, `shutil`, `subprocess`.
    *   **Data Serialization**: `json`, `csv`, `pickle`.
    *   **Networking**: `urllib`, `http`.
    *   **Concurrency**: `threading`, `multiprocessing`, `asyncio`, `concurrent.futures`.
    *   **Config & CLI**: `dotenv`, `argparse`, `configparser`, `logging`, `re`.

### 🗄️ 3. Database Operations (SQLite)
*   **[DB_OPs](./DB_OPs/)**: "Zero to Hero" guide for SQL with Python.
    *   **Basics**: Connection, table creation, and CRUD operations.
    *   **Relational**: Foreign keys, Joins, and relationships.
    *   **Advanced**: Transactions, Rollbacks, Performance Indexing, and custom Python-SQL functions.
    *   **Exports**: Exporting SQL data to CSV and JSON.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher.
- `pip` (Python package manager).

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Install recommended third-party libraries for full demo functionality:
   ```bash
   pip install python-dotenv requests
   ```

### Running the Demos
Each directory contains self-contained scripts. You can run any demo directly from the terminal:
```bash
# Example: Running the SQLite Advanced demo
python DB_OPs/05_advanced.py

# Example: Running the Library Concurrency demo
python library/26_asyncio_demo.py
```

---

## 🌟 Highlights
- **Best Practices**: All SQL queries use parameterized inputs to prevent SQL injection.
- **Modern Standards**: Usage of `pathlib` for OS-agnostic path handling.
- **Professional Patterns**: Implementation of custom context managers and decorators.
- **Scalability**: Demonstrations of parallel processing and asynchronous programming.

---

## 📝 Author
Created with ❤️ for the Python community. Happy coding!
