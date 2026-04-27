# 📚 The Python Standard Library Masterclass

This directory is a comprehensive manual for Python's built-in batteries. From high-speed math to asynchronous I/O and CLI building, these scripts demonstrate the core tools every Data Scientist and Software Engineer should master.

---

## 🗺️ Learning Roadmap

### 🧮 Data & Mathematics
| File | Module | Key Features |
| :--- | :--- | :--- |
| `01_math_demo.py` | `math` | Constants (π, e), trigonometry, and power functions. |
| `02_statistics_demo.py`| `statistics` | Mean, median, mode, and standard deviation. |
| `03_random_demo.py` | `random` | Shuffling, sampling, and uniform/gaussian distributions. |
| `08_heapq_demo.py` | `heapq` | Implementing priority queues with min-heaps. |
| `09_bisect_demo.py` | `bisect` | Maintaining binary search efficiency in sorted lists. |

### ⚡ Functional & Iterative Tools
| File | Module | Key Features |
| :--- | :--- | :--- |
| `04_itertools_demo.py` | `itertools` | Infinite iterators, permutations, and combinations. |
| `05_functools_demo.py` | `functools` | `@lru_cache`, `partial` functions, and `reduce`. |
| `06_collections_demo.py`| `collections`| `Counter`, `deque`, `namedtuple`, and `defaultdict`. |
| `07_operator_demo.py` | `operator` | Functional interface to built-in operators. |

### 📁 Filesystem & System Control
| File | Module | Key Features |
| :--- | :--- | :--- |
| `13_os_demo.py` | `os` | Environment variables, directories, and file removal. |
| `14_sys_demo.py` | `sys` | Command-line args, recursion limits, and path control. |
| `15_pathlib_demo.py` | `pathlib` | Modern, object-oriented path manipulation. |
| `16_shutil_demo.py` | `shutil` | High-level file copying, moving, and archiving. |
| `18_subprocess_demo.py`| `subprocess`| Running shell commands and capturing output. |

### 🌐 Data Serialization & Networking
| File | Module | Key Features |
| :--- | :--- | :--- |
| `10_json_demo.py` | `json` | Parsing and serializing JSON data. |
| `22_csv_demo.py` | `csv` | Reading/Writing tabular data. |
| `23_pickle_demo.py` | `pickle` | Native Python object serialization. |
| `11_urllib_demo.py` | `urllib` | Requesting data from URLs. |
| `12_http_demo.py` | `http` | Low-level HTTP client and server tools. |

### 🕒 Time, Logging & Configuration
| File | Module | Key Features |
| :--- | :--- | :--- |
| `20_time_demo.py` | `time` | Epoch timestamps and performance counters. |
| `21_datetime_demo.py` | `datetime` | Timezone-aware date and time math. |
| `28_dotenv_demo.py` | `dotenv` | Securely loading `.env` secrets from `envs/`. |
| `30_logging_demo.py` | `logging` | Debug, Info, Warning, Error, and Critical streams. |
| `31_argparse_demo.py` | `argparse` | Creating professional CLI tools with Help menus. |
| `32_configparser_demo.py`| `configparser`| Working with `.ini` configuration files. |

### 🚦 Concurrency & Advanced
| File | Module | Key Features |
| :--- | :--- | :--- |
| `24_threading_demo.py` | `threading` | Shared memory concurrency (IO-bound). |
| `25_multiprocessing.py`| `multiprocessing`| Process-based parallelism (CPU-bound). |
| `26_asyncio_demo.py` | `asyncio` | Single-threaded concurrent Coroutines. |
| `29_re_demo.py` | `re` | Mastering Regular Expressions for text mining. |

---

## 🛠️ Setup & Execution

1. **Environment**: Ensure you have `python-dotenv` installed for the `.env` demo.
   ```bash
   pip install python-dotenv
   ```
2. **Secrets**: Professional apps keep secrets in the `envs/` folder. Check `envs/.env.example` for the required format.
3. **Running**: Execute any script individually to see its focused demonstration.
   ```bash
   python 04_itertools_demo.py
   ```

---

> [!IMPORTANT]
> **Pro Tip**: Use `pathlib` instead of `os.path` for new projects. It's more readable, cross-platform, and handles edge cases automatically!

---
*Part of the "Zero to Data Scientist" Python Advanced Series.*
