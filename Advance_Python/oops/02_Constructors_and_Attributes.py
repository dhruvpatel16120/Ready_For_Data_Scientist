# 🎓 Lesson 02: Constructors and Attributes
# 🏛️ Topic: __init__ types and Variable Scoping

class Employee:
    # 🌍 CLASS VARIABLE
    # Shared by all instances. Useful for constants like company name.
    company_name = "Tech Solutions Inc."
    total_employees = 0

    # 🛠️ 1. PARAMETERIZED CONSTRUCTOR
    def __init__(self, name, salary):
        # 🆔 INSTANCE VARIABLES
        # Unique to each employee
        self.name = name
        self.salary = salary
        
        # Updating a class variable using the Class name
        Employee.total_employees += 1
        print(f"Constructed: {self.name}")

    # 🛠️ 2. DEFAULT CONSTRUCTOR
    # NOTE: Python doesn't support multiple __init__ methods in one class.
    # But we can simulate a 'Non-Parameterized' constructor by giving default values:
    # def __init__(self, name="Guest", salary=0): ...

    def display(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {Employee.company_name}")

# --- EXECUTION ---

# Create objects using Parameterized Constructor
emp1 = Employee("Alice", 70000)
emp2 = Employee("Bob", 80000)

emp1.display()
emp2.display()

# 🔍 ACCESSING VARIABLES
print(f"\nTotal Employees (Class Variable): {Employee.total_employees}")

# ⚠️ Modifying Class Variable for ALL instances
Employee.company_name = "Global Tech"
print(f"Updated Company (for Alice): {emp1.company_name}")
print(f"Updated Company (for Bob): {emp2.company_name}")

# 🔬 Modifying Instance Variable (ONLY for Bob)
emp2.salary = 85000
print(f"Bob's New Salary: {emp2.salary}")
print(f"Alice's Salary (remains same): {emp1.salary}")
