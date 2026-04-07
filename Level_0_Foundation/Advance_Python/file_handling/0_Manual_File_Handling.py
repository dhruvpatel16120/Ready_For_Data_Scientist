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
print("\n")
# READING functions for File Handling

# 1. read() - Reads the entire file content as a single string
# 2. readline() - Reads a single line from the file
# 3. readlines() - Reads all lines from the file and returns them as a list of strings

# read whole file
file = open(filename, "r")
print("\n--- Reading whole file ---")
print(file.read())
file.close()

# read specific number of characters from file
file = open(filename, "r")
print("\n--- Reading specific number of characters ---")
print(file.read(5))
file.close()

# read one line of file  
file = open(filename, "r")
print("\n--- Reading one line of file ---")
print(file.readline())
file.close()

# read all lines of file and return list of strings
file = open(filename, "r")
print("\n--- Reading all lines of file ---")
print(file.readlines())
file.close()

# WRITING functions for File Handling
# it overwrite the file if file is already exists
# Note: write() and writelines() does not add newline characters automatically.
# 1. write() - Writes a string to the file
# 2. writelines() - Writes a list of strings to the file

print("\n--- WRITING functions for File Handling ---")
# write to file
print("\n--- Writing to file ---")
file = open(filename, "r")
print("file content before write() method:")
print(file.read())
file.close()
file = open(filename, "w")
file.write("\"This file was written using write() method.\"\n")
print("file content after write() method:")
file = open(filename, "r")
print(file.read())
file.close()

# position of file pointer
file = open(filename, "r")
print("position of file pointer before read() method:", file.tell())
print(file.read())
print("position of file pointer after read() method:", file.tell(),'\n')
file.close()

# write multiple lines to file
file = open(filename,"r")
print("file content before writelines() method:")
print(file.read())
file.close()
file = open(filename, "w")
print("\n--- Writing multiple lines to file ---")
file.writelines(["This is line 1.\n", "This is line 2.\n", "This is line 3.\n"])
file.close()
file = open(filename,"r")
print("file content after writelines() method:")
print(file.read())
file.close()


# 1. seek() - Moves the file pointer to a specific position
# 2. tell() - Returns the current position of the file pointer
# 3. flush() - Flushes the file buffer (forces data to be written to the file)

print("\n--- SEEKING and TELLING functions for File Handling ---")
# seek to specific position
file = open(filename, "r")
print("\n--- Seeking to specific position ---")
print(file.read())
file.seek(10)
print("position of file pointer after seek() method:", file.tell())
file.close()

# flush the file buffer . flush() is used to write the data from the buffer to the file. 
# where buffer is the temporary storage area where the data is stored before being written to the file.

file = open(filename, "w")
file.write("This is a test string.")
file.flush()
file.close()