# 🎓 Lesson 08: Magic Methods and Destructors
# 🏛️ Topic: Dunder (Double Under) Methods

class SmartVector:
    # 1. CONSTRUCTOR
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"Object ({self.x}, {self.y}) created.")

    # 2. STRING REPRESENTATION (__str__)
    # Controls what 'print(object)' shows.
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # 3. ADDITION OVERLOADING (__add__)
    # Allows using '+' operator between objects.
    def __add__(self, other):
        return SmartVector(self.x + other.x, self.y + other.y)

    # 4. LENGTH (__len__)
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)

    # 5. DESTRUCTOR (__del__)
    # Called when an object is deleted or program ends.
    def __del__(self):
        print(f"Cleanup: Destructing Vector({self.x}, {self.y})")

# --- EXECUTION ---

v1 = SmartVector(3, 4)
v2 = SmartVector(1, 2)

# Using __str__
print(f"Vector 1: {v1}")

# Using __add__ (This is also Operator Overloading)
v3 = v1 + v2
print(f"Combined Vector: {v3}")

# Using __len__
print(f"Magnitude (len) of V1: {len(v1)}")

# Triggering Destructor manually (or just wait for script to end)
del v2
print("End of script reached.")
