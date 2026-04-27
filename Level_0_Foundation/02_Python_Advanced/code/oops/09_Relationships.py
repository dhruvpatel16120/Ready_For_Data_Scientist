# 🎓 Lesson 09: Object Relationships
# 🏛️ Topic: Association, Aggregation, and Composition

"""
1. ASSOCIATION: A loose relationship. No ownership. (Teacher and Student)
2. AGGREGATION: "Has-A" relationship. Weak ownership. Parts can exist without whole. (Library and Books)
3. COMPOSITION: "Part-Of" relationship. Strong ownership. Parts DIE if whole dies. (House and Rooms)
"""

# --- 1. AGGREGATION ---
class Salary:
    def __init__(self, basic, bonus):
        self.basic = basic
        self.bonus = bonus
    
    def get_total(self):
        return self.basic + self.bonus

class Employee:
    def __init__(self, name, salary_obj):
        self.name = name
        # Employee 'HAS-A' Salary (Aggregation)
        self.salary = salary_obj 

# --- 2. COMPOSITION ---
class Engine:
    def start(self):
        print("Engine Revving... Broom Broom!")

class Car:
    def __init__(self):
        # Car contains Engine (Composition)
        # If Car is deleted, this Engine object is lost too.
        self.engine = Engine()

    def start_car(self):
        print("Starting car...")
        self.engine.start()

# --- EXECUTION ---

print("--- Aggregation Demo ---")
sal = Salary(50000, 5000) # Salary exists independently
emp = Employee("Alice", sal) # Linked to Employee
print(f"Employee {emp.name} Salary: {emp.salary.get_total()}")
# If 'emp' is deleted, 'sal' still exists in memory!

print("\n--- Composition Demo ---")
my_car = Car()
my_car.start_car()
# If 'my_car' is deleted, the Engine instance created INSIDE it dies too.

# --- ASSOCIATION (Visual Example only) ---
class Student: pass
class Teacher:
    # A teacher can have students, but neither owns the other.
    def add_student(self, student): pass 
