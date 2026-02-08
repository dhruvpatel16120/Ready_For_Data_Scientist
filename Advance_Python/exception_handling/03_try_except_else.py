"""
03: Try-Except-Else
===================

The 'else' block runs ONLY if the 'try' block completes without raising any 
exceptions. This is useful for code that should only execute if the 
risky operation was successful.
"""

print("--- [03] Try-Except-Else Demo ---")

def divide(a, b):
    try:
        print(f"Dividing {a} by {b}...")
        res = a / b
    except ZeroDivisionError:
        print("❌ Error: Division by zero!")
    else:
        # This code runs only if NO error occurred
        print(f"✅ Calculation successful! Result: {res}")
        return res

# Case 1: Success
divide(10, 2)

# Case 2: Failure
print("-" * 30)
divide(10, 0)
