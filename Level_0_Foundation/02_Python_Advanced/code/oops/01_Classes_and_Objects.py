# 🎓 Lesson 01: Classes and Objects - The Foundation of OOP
# =========================================================

"""
CONCEPT:
A Class is a 'blueprint' or 'template' for creating objects.
An Object is an 'instance' of a class. (Real-world entity)

Analogy: 
Class: A Drawing of a House (Specs: rooms, windows, color)
Object: The Actual House built from that drawing.
"""

# 🏛️ 1. Defining a Class
class Student:
    """
    This class represents a Student.
    It contains data (attributes) and behavior (methods).
    """
    
    # 属性 (Attributes/Data) - Hardcoded for now (bad practice, but good for learning)
    school_name = "Oxford International" # Class Attribute (Shared by all)

    # 🛠️ 2. The Method (Behavior)
    # 'self' is a reference to the specific object being created/accessed.
    # It must be the first parameter in any instance method.
    def welcome(self):
        print(f"Welcome to {self.school_name}!")

    def info(self, name, age):
        # We can pass data to methods
        print(f"Student Name: {name}")
        print(f"Student Age: {age}")

# 🚀 3. Creating an Object (Instantiating)
# student1 is an object of the Student class.
student1 = Student()

# 🔍 4. Accessing Attributes and Methods using the 'Dot' (.) operator
print("--- Instance 1 ---")
print(f"School: {student1.school_name}")
student1.welcome()
student1.info("Karan", 21)

# 🚀 5. Creating multiple objects from the SAME class
student2 = Student()
print("\n--- Instance 2 ---")
student2.info("Arjun", 22)

class Car:
    def __init__(self):
        self._brand = "Toyota"
        self._model = "Camry"
        self._year = 2022
        # self._brand = "Toyota"
        # self._model = "Camry"
        # self._year = 2022
    
    def display(self):
        print(f"Brand: {self._brand}")
        print(f"Model: {self._model}")
        print(f"Year: {self._year}")

car1 = Car()
car1.display()
# print(car1.brand) # it will give error because it is protected and not publicly accessible outside the class
# print(car1.model) # it will give error because it is protected and not publicly accessible outside the class
# print(car1.year) # it will give error because it is protected and not publicly accessible outside the class
print(car1._brand) # it will access because it is protected, but it is not recommended to access it outside the class
print(car1._model) # it will access because it is protected, but it is not recommended to access it outside the class
print(car1._year) # it will access because it is protected, but it is not recommended to access it outside the class

# 💡 KEY TAKEAWAYS:
# 1. Class: The Blueprint (Student)
# 2. Object: The Reality (student1, student2)
# 3. Method: The Action (welcome, info)
# 4. Attribute: The Data (school_name)
# 5. self: Points to the current object instance.
