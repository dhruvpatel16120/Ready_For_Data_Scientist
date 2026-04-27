"""
02: Try-Except Block
====================

The try-except block is the foundation of error handling in Python.
- 'try': Code that might fail.
- 'except': Code that runs if a failure occurs.

You can catch specific exceptions or multiple exceptions at once.
"""

print("--- [02] Try-Except Demo ---")

# 1. Catching a specific exception
try:
    result = 10 / 0
except ZeroDivisionError:
    print("❌ Error: Cannot divide by zero.")

# 2. Catching multiple exceptions
try:
    num = int("abc") # This will raise a ValueError
except (ValueError, TypeError) as e:
    print(f"❌ Error caught: {e}")

# 3. Catch-all Exception (Use sparingly!)
try:
    # Some risky code
    import google.generativeai

except Exception as e:
    print(f"❌ An unexpected error occurred: {type(e).__name__} - {e}")

print("\nProgram finished successfully.")
