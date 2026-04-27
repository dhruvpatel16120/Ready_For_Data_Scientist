# 🏗️ Mastery: Object-Oriented Programming (OOP)

Welcome to the **OOP Masterclass**! This module is designed to transform the way you think about code. Instead of writing sequences of instructions, you will learn to build **blueprints** for the real world, creating software that is modular, scalable, and easy to maintain.

---

## 🏛️ The Four Pillars of OOP

Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data (attributes) and code (methods). It helps in organizing complex software into reusable and modular components.

Mastering OOP requires understanding four fundamental principles that govern how objects interact:

- **🔐 Encapsulation**: Bundling data (attributes) and behavior (methods) into a single unit while restricting direct access to combat complexity.
- **🧬 Inheritance**: Creating a hierarchy where child classes reuse and extend the logic of parent classes, reducing redundancy.
- **🎭 Polymorphism**: The ability of different objects to respond to the same method call in their own unique way.
- **👻 Abstraction**: Hiding implementation details and exposing only the essential interface to the user.

---

## 🗺️ Learning Roadmap

| Stage  | Lesson                      | Core Learning Objective                                                  |
| :----- | :-------------------------- | :----------------------------------------------------------------------- |
| **01** | `01_Classes_and_Objects.py` | Defining blueprints and creating your first instances.                   |
| **02** | `02_Constructors.py`        | Master `__init__` and differentiate between Instance & Class variables.  |
| **03** | `03_Methods_Types.py`       | Understanding Instance, `@classmethod`, and `@staticmethod`.             |
| **04** | `04_Encapsulation.py`       | Using Public, Protected, and Private access to secure data.              |
| **05** | `05_Inheritance_Types.py`   | From Single to Hybrid inheritance patterns.                              |
| **06** | `06_Polymorphism.py`        | Overriding methods and the nuances of Python "overloading."              |
| **07** | `07_Abstraction.py`         | Building contracts using the `abc` (Abstract Base Class) module.         |
| **08** | `08_Magic_Methods.py`       | Deep dive into Dunder methods like `__str__`, `__repr__`, and `__add__`. |
| **09** | `09_Relationships.py`       | Defining how objects connect (Aggregation & Composition).                |
| **10** | `10_access_modifiers.py`    | Practical implementation of Python's data hiding conventions.            |

---

## 🚀 Why OOP for Data Science?

In Data Science, OOP is used to build robust machine learning pipelines:

- **Scikit-learn**: Every model (LinearRegression, KMeans) is a Class.
- **PyTorch/TensorFlow**: Neural networks are defined by inheriting from `nn.Module`.
- **Pandas**: DataFrames are complex objects with hundreds of specialized methods.

Understanding OOP allows you to read professional library source code and build your own custom estimators and data transformers.

---

## 🛠️ Usage

Each script is a standalone lesson. Run them sequentially to build your knowledge:

```powershell
python 01_Classes_and_Objects.py
python 02_Constructors_and_Attributes.py
# ... and so on
```

---

> [!TIP]
> **Pro Tip**: In Python, "Private" attributes (like `__name`) aren't truly private—they are just "name mangled." Use them as a signal to other developers that the attribute is internal, not as a foolproof security measure!

---

_Part of the "Zero to Data Scientist" Python Advanced Series._
