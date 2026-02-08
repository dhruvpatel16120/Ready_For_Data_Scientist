"""
01: Raising Exceptions
=====================

The 'raise' keyword is used to manually trigger an exception when a specific 
condition is met in your code. This is useful for validation or forcing 
a program to stop when it reaches an invalid state.

Syntax:
raise ExceptionType("Optional error message")
"""

def check_age(age):
    if age < 0:
        # Manually raising a built-in exception
        raise ValueError("Age cannot be negative.")
    if age > 150:
        raise ValueError("Age is too high for a human.")
    print(f"Age {age} is valid.")

print("--- [01] Raising Exceptions Demo ---")

try:
    user_age = 185
    print(f"Checking age: {user_age}...")
    check_age(user_age)
except ValueError as e:
    print(f"Caught an error: {e}")
    # Another example: Raising generic Exception
    # raise Exception("Something went wrong!")
