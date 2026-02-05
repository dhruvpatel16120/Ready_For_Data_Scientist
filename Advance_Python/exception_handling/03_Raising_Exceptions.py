# 03_Raising_Exceptions.py
# Level: 🟠 Advanced
# Topic: Using 'raise' to trigger your own errors

"""
Sometimes we want to create our own error conditions, even if 
Python's syntax is technically correct.
"""

def set_age(age):
    if age < 0:
        # Manually triggering a ValueError
        raise ValueError("Age cannot be negative!")
    if age > 120:
        raise ValueError("That age seems unrealistic for a human.")
    print(f"Age set to: {age}")

print("--- Raising Exceptions ---")

try:
    user_age = int(input("Enter your age: "))
    set_age(user_age)
except ValueError as e:
    # 'e' contains the message we put in the 'raise' statement
    print(f"⚠️  Validation Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
