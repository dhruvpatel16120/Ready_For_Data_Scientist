# 🎓 Lesson 01: Classes and Objects
# 🏛️ Topic: Understanding the Blueprint and the Instance

"""
CLASS: A logical grouping of data and functions. It's a template or blueprint.
OBJECT: A physical entity created from a class. It holds real data.
"""

class Car:
    """A simple class to represent a car."""
    pass # 'pass' is used to create an empty class for later use

# 1. Creating Objects (Instances)
car1 = Car()
car2 = Car()

# 2. Assigning attributes dynamically (Not recommended in professional code, but possible in Python)
car1.brand = "Tesla"
car1.model = "Model S"

print(f"Car 1: {car1.brand} {car1.model}")

# 🚀 PROPER APPROACH: Define attributes inside the class structure
class Book:
    def __init__(self, title, author):
        # Attribute assignment
        self.title = title
        self.author = author

    def get_info(self):
        return f"'{self.title}' by {self.author}"

# Creating objects properly
book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("Clean Code", "Robert C. Martin")

print(f"Book 1: {book1.get_info()}")
print(f"Book 2: {book2.get_info()}")

# 🔍 Key Takeaway:
# 'self' is a reference to the current instance of the class. 
# It allows us to access variables that belong to the class.
