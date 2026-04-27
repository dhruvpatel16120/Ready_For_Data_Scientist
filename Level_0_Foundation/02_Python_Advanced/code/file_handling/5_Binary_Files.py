# File: 5_Binary_Files.py
# Demonstration of Binary file operations (.bin / .dat) using pickle
# Binary files are used to save Python objects exactly as they are.
import pickle

filename = "Level_0_Foundation/02_Python_Advanced/code/file_handling/test_file/data.bin"

# A list of complex Python objects
data_to_store = {
    "list": [1, 2, 3, 4],
    "tuple": ("A", "B", "C"),
    "number": 100.5,
    "active": True
}
 
# 1. Writing to a Binary file
# 'wb' mode: Write Binary
print("--- Writing to a binary file ---")
with open(filename, "wb") as file:
    pickle.dump(data_to_store, file)
    print(f"Object serialized and saved to {filename}")

# 2. Reading from a Binary file
# 'rb' mode: Read Binary
print("\n--- Reading from a binary file ---")
with open(filename, "rb") as file:
    loaded_data = pickle.load(file)
    print("Loaded Data from binary file:")
    print(loaded_data)
    print(f"Accessing list: {loaded_data['list']}")

# 3. Handling Image/Other Binary files
# This is how you would copy an image or binary file
# with open("source.png", "rb") as source:
#     data = source.read()
#     with open("destination.png", "wb") as dest:
#         dest.write(data)
# print("\nBinary copy logic commented out in script.")
