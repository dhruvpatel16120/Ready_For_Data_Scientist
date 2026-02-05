# Importing the user-defined module 'utils' that is from utils.py
import utils

# Alternatively, you can import specific items:
# from utils import greet, PI_VALUE

print("--- User-Defined Module Demo ---")

# Using functions from the imported module
message = utils.greet("Student")
print(message)

result = utils.add_numbers(10, 25)
print(f"Result of adding numbers using utils: {result}")

# Accessing variables from the imported module
print(f"PI Value from utils: {utils.PI_VALUE}")

print("\nNote: The 'utils.py' file must be in the same directory or in the Python path.")
