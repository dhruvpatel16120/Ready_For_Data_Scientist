# File: 1_Text_Files.py
# Demonstration of basic text file operations (.txt)

filename = "Advance_Python/file_handling/example.txt"

# 1. Writing to a text file
# 'w' mode: writes new content, overwrites if file exists
print("--- Writing to a text file ---")
with open(filename, "w") as file:
    file.write("Hello! This is a simple text file.\n")
    file.write("Python makes file handling very easy.\n")
    print(f"Content written to {filename}")

# 2. Reading from a text file
# 'r' mode: reads the content
print("\n--- Reading from a text file ---")
with open(filename, "r") as file:
    content = file.read()
    print("File Content:")
    print(content)

# 3. Appending to a text file
# 'a' mode: adds content to the end of the file
print("\n--- Appending to a text file ---")
with open(filename, "a") as file:
    file.write("This line was added using append mode.\n")
    print("New line appended.")

# 4. Reading line by line
print("\n--- Reading file line by line ---")
with open(filename, "r") as file:
    for line in file:
        print(f"Line: {line.strip()}")
