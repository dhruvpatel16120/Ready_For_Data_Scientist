# File: 0_Manual_File_Handling.py
# Demonstration of file operations WITHOUT 'with' statement
# This method requires manually closing the file using .close()

filename = "Advance_Python/file_handling/manual_example.txt"

# 1. Writing to a file manually
print("--- Writing without 'with' statement ---")
file = open(filename, "w")  # Open file in write mode
file.write("This file was opened manually.\n")
file.write("It must be closed manually too!\n")
file.close()  # VERY IMPORTANT: Close the file to save changes and free memory
print(f"File {filename} written and closed.")

# 2. Reading from a file manually
print("\n--- Reading without 'with' statement ---")
file = open(filename, "r")  # Open file in read mode
content = file.read()
print("File Content:")
print(content)
file.close()  # Close the file after reading
print("File closed after reading.")

# 3. Handling errors manually (The old way)
print("\n--- Manual Handling with Exception ---")
try:
    file = open(filename, "r")
    # Perform operations
    data = file.read()
    print("Successfully read data using try-finally.")
finally:
    # This block always runs, ensuring the file is closed even if an error occurs
    file.close()
    print("File closed safely in 'finally' block.")

print("\nNote: The 'with' statement is usually preferred because it closes the file automatically.")
