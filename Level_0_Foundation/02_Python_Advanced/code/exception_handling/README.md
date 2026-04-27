# ⚠️ Mastery: Python Exception Handling

Welcome to the **Exception Handling** module! In the world of Data Science and Engineering, things will break: files will be missing, connections will time out, and data will be malformed. This module teaches you how to build **resilient** Python applications that handle errors gracefully instead of crashing.

---

## 🗺️ Module Curriculum

| Stage | File | Focus Area |
| :--- | :--- | :--- |
| **01** | `01_raising_exception.py` | **Triggering Errors**: Using the `raise` keyword to signal issues. |
| **02** | `02_try_except.py` | **Defensive Coding**: catching and handling specific exceptions. |
| **03** | `03_try_except_else.py` | **Positive Path**: Using `else` for code that runs only on success. |
| **04** | `04_try_except_finally.py`| **Cleanup**: Using `finally` for guaranteed resource release. |
| **05** | `05_custom_exception.py` | **Specialize**: Creating domain-specific error types for your apps. |

---

## 🔄 The Exception Lifecycle

Understanding the flow of control is key to mastering error handling:

```python
try:
    # 🏃 1. Primary logic here (might fail)
except ValueError:
    # 🛑 2a. Runs ONLY if a ValueError occurred
else:
    # ✅ 2b. Runs ONLY if NO exceptions occurred in 'try'
finally:
    # 🧹 3. ALWAYS runs (cleanup, closing files, etc.)
```

---

## 🏗️ Deep Dive: The Hierarchy

Python exceptions are not flat list; they are organized in a **Hierarchy**. This means catching a parent exception (like `LookupError`) will also catch its children (like `IndexError` and `KeyError`).

Check out the **[Python Exception Hierarchy Reference](./Python_Exception_Hierarchy.md)** for a visual guide and complete list of built-in errors.

---

## 🚀 How to Run

Execute the scripts sequentially to see how different blocks interact:

```powershell
python 02_try_except.py
python 03_try_except_else.py
# ... and so on
```

---

> [!IMPORTANT]
> **Data Science Tip**: When processing large datasets, use exception handling inside your loops to log "bad rows" instead of letting one bad value terminate a 10-hour training job!

---
*Created as part of the "Zero to Data Scientist" Foundation Series.*
