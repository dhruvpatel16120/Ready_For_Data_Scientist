# 01_Basic_Try_Except.py
# Level: 🟢 Beginner
# Topic: The Fundamental Try-Except Block

"""
Exception handling is used to prevent the program from crashing 
when an error occurs.
"""

print("--- Basic Exception Handling ---")

try:
    # 1. Catching multiple specific exceptions
    number = int(input("Enter a number to divide 100: "))
    
    # 2. The 'Throw' Concept (Using 'raise' in Python)
    # We can manually trigger an exception if a condition is met
    if number == 5:
        # In other languages this is called 'throwing' an error
        raise ValueError("Sorry, I just don't like the number 5!")
        
    result = 100 / number
    print(f"Success! Result is {result}")

except (ZeroDivisionError, TypeError):
    # 3. Multiple exceptions in one block
    print("❌ Error: Math error or Invalid Type occurred.")

except ValueError as e:
    # 4. Using 'as' to get the error message (Aliasing)
    print(f"❌ Value Error: {e}")

except Exception as e:
    # 5. Catch-All: Catching any other unexpected error
    print(f"❌ An unexpected error occurred: {e}")

print("\nProgram continues running...")
