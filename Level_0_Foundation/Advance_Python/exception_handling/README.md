# Python Exception Handling Mastery

This directory contains a complete "Zero to Hero" guide for handling errors and exceptions in Python. Exception handling ensures your program doesn't crash unexpectedly and allows for safe resource cleanup.

## 📂 Contents

| File | Topic | Description |
|------|-------|-------------|
| **[01_raising_exception.py](./01_raising_exception.py)** | Raising Exceptions | How to manually trigger errors using `raise`. |
| **[02_try_except.py](./02_try_except.py)** | Try-Except Block | The core syntax for catching and handling errors. |
| **[03_try_except_else.py](./03_try_except_else.py)** | The Else Block | Code that runs ONLY when no exceptions occur. |
| **[04_try_except_finally.py](./04_try_except_finally.py)** | The Finally Block | Guaranteed code execution (ideal for cleanup). |
| **[05_custom_exception.py](./05_custom_exception.py)** | Custom Exceptions | Creating user-defined error types for specialized logic. |

---

## 🚀 Getting Started

To explore these examples, run them in order:

```powershell
python 01_raising_exception.py
python 02_try_except.py
python 03_try_except_else.py
python 04_try_except_finally.py
python 05_custom_exception.py
```

## 🧠 Key Concepts

1. **Try**: Encapsulates code that might fail.
2. **Except**: Handles specific errors.
3. **Else**: Executes if the try block was successful.
4. **Finally**: Always executes, useful for closing files or connections.
5. **Raise**: Manually triggers a specific exception.
