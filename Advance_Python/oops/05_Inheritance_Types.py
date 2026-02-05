# 🎓 Lesson 05: Inheritance
# 🏛️ Topic: 5 Types of Inheritance in Python

# --- 1. SINGLE INHERITANCE ---
class Parent:
    def func1(self):
        print("Function 1 from Parent")

class Child(Parent):
    def func2(self):
        print("Function 2 from Child")

# --- 2. MULTIPLE INHERITANCE ---
class Father:
    def strength(self):
        print("Father's Strength")

class Mother:
    def wisdom(self): 
        print("Mother's Wisdom")

class Son(Father, Mother):
    def skills(self): 
        print("Son's combined skills")

# --- 3. MULTILEVEL INHERITANCE ---
class Grandfather:
    def farm(self): print("Grandfather's Farm")

class Dad(Grandfather):
    def office(self): print("Dad's Office")

class Junior(Dad):
    def school(self): print("Junior's School")

# --- 4. HIERARCHICAL INHERITANCE ---
class Vehicle:
    def move(self): print("Vehicle Moving")

class Car(Vehicle):
    def horn(self): print("Beep Beep")

class Bike(Vehicle):
    def bell(self): print("Tring Tring")

# --- 5. HYBRID INHERITANCE (Diamond Pattern) ---
# A mix of Multiple and Multilevel
class A:
    def show(self): print("Class A")

class B(A):
    def show(self): print("Class B")

class C(A):
    def show(self): print("Class C")

class D(B, C):
    pass

# --- DEMONSTRATION ---

print("--- Multilevel Demo ---")
j = Junior()
j.farm()   # From Grandfather
j.office() # From Dad
j.school() # From Junior

print("\n--- Multiple Demo ---")
s = Son()
s.strength()
s.wisdom()

print("\n--- MRO (Method Resolution Order) ---")
# Special attribute to see how Python looks for methods in Hybrid Inheritance
print(D.mro())
d = D()
d.show() # Will choose Class B first (Left to Right)
