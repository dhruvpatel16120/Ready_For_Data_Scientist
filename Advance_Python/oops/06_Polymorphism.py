# 🎓 Lesson 06: Polymorphism
# 🏛️ Topic: Method Overriding and Overloading

"""
POLYMORPHISM: The ability to take different forms.
In Python, this usually happens via:
1. Method Overriding (Dynamic/Runtime Polymorphism)
2. Method Overloading (Static Polymorphism - Simulated in Python)
"""

# --- 1. METHOD OVERRIDING ---
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self): # Overriding parent's method
        print("🐶 Dog barks: Woof Woof!")

class Cat(Animal):
    def speak(self): # Overriding parent's method
        print("🐱 Cat meows: Meow!")

# --- 2. METHOD OVERLOADING ---
# Strictly speaking, Python doesn't support method overloading (multiple methods with same name).
# But we can simulate it using default arguments or *args.

class Calculator:
    # Simulating Overloading
    def add(self, a, b, c=0):
        return a + b + c

# --- 3. DUCK TYPING (Polymorphism in Practice) ---
def animal_test(animal_obj):
    animal_obj.speak() # Doesn't care about class, only if it has 'speak()'

# --- EXECUTION ---

print("--- Overriding Demo ---")
my_dog = Dog()
my_cat = Cat()

animal_test(my_dog)
animal_test(my_cat)

print("\n--- Overloading Simulation ---")
calc = Calculator()
print(f"2 numbers: {calc.add(10, 20)}")
print(f"3 numbers: {calc.add(10, 20, 30)}")

# 🔍 Key Point:
# 'super()' can be used inside overridden methods to still call the parent version.
class RoboCat(Cat):
    def speak(self):
        super().speak() # Call Cat meow
        print("🤖 ...and beeps robotically.")

r = RoboCat()
r.speak()
