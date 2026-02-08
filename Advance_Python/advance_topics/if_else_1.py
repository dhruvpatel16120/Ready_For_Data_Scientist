"""
Python Ternary Operator (If-Else in One Line)
============================================

The ternary operator allows you to assign a value based on a condition 
in a single line. It's more concise than a traditional if-else block.

Syntax:
[value_if_true] if [condition] else [value_if_false]
"""

# --------------------------------------------------------------------------
# 1. Basic Usage
# --------------------------------------------------------------------------
age = 20
status = "Adult" if age >= 18 else "Minor"

print(f"[1] Basic Ternary: age={age} -> {status}")

# --------------------------------------------------------------------------
# 2. Used in Print Statements
# --------------------------------------------------------------------------
score = 85
print(f"[2] Print Test: {'Passed' if score >= 40 else 'Failed'} with {score}")

# --------------------------------------------------------------------------
# 3. Handling None Values (Defaulting)
# --------------------------------------------------------------------------
user_input = None
display_name = user_input if user_input is not None else "Guest"
print(f"[3] Defaulting: {display_name}")

# --------------------------------------------------------------------------
# 4. Nested Ternary Operators (Use sparingly for readability!)
# --------------------------------------------------------------------------
# Find the largest of three numbers
a, b, c = 10, 20, 15
largest = a if (a > b and a > c) else (b if b > c else c)
print(f"[4] Nested Ternary: Largest of {a}, {b}, {c} is {largest}")

# --------------------------------------------------------------------------
# 5. Using Ternary with Functions
# --------------------------------------------------------------------------
def get_discount(is_member):
    return 20 if is_member else 0

print(f"[5] Function Return: Member discount is {get_discount(True)}%")

# --------------------------------------------------------------------------
# 6. Alternative: Tuple-based (Not recommended, but exists)
# --------------------------------------------------------------------------
# Syntax: (value_if_false, value_if_true)[condition]
# Condition must result in 0 (False) or 1 (True)
is_active = True
mode = ("Offline", "Online")[is_active]
print(f"[6] Tuple-based Ternary: {mode}")

# --------------------------------------------------------------------------
# 7. Alternative: Dictionary-based
# --------------------------------------------------------------------------
user_role = "admin"
access_level = {"admin": "Full", "user": "Limited"}.get(user_role, "None")
print(f"[7] Dictionary-based: {access_level}")

# --------------------------------------------------------------------------
# 8. Practical Example: List Comprehensions
# --------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6]
# Label numbers as Even or Odd
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print(f"[8] list Comprehension: {labels}")

if __name__ == "__main__":
    print("\n✅ Ternary Operator demonstrations complete.")
