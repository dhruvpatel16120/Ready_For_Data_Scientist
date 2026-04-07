import glob

"""
Python glob Module
Finds all the pathnames matching a specified pattern according to the rules used by the Unix shell.
"""

print("Files in current dir:")
print(glob.glob("*"))

print("--- Listing all .py files ---")
py_files = glob.glob("**/*.py")
print(py_files)

print("\n--- Listing 0x_ prefix files ---")
prefix_files = glob.glob("**/0[1-5]_*.py")
print(prefix_files)

print("\n--- Iterating with iglob (efficient iterator) ---")
for name in glob.iglob("*_demo.py"):
    print(f"Found: {name}")

# Recursive search (since Python 3.5)
# print("\n--- Recursive search ---")
# all_files = glob.glob("**/*.py", recursive=True)
# print(all_files)
