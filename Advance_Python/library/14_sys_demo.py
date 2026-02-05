import sys

"""
Python sys Module
Provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
"""

# 1. Command-line arguments
print(f"Script Name: {sys.argv[0]}")
print(f"Arguments passed: {sys.argv[1:]}")

# 2. Path and Platform info
print(f"\nPython Version: {sys.version}")
print(f"Platform: {sys.platform}")
print(f"Executable: {sys.executable}")
# print(f"Module Search Path: {sys.path[:3]}...")

# 3. Memory Usage
x = [1, 2, 3, 4, 5]
print(f"\nSize of list x in bytes: {sys.getsizeof(x)}")

# 4. Standard Streams (usually handled by print/input)
sys.stdout.write("Writing to standard output via sys.stdout\n")
# sys.stderr.write("This is an error message\n")

# 5. Exit
# sys.exit(0) # Standard ways to exit a script
