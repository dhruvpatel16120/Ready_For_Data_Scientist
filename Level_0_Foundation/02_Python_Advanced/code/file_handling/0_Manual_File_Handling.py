"""
0: Modular File Handling Demo
=============================
This script demonstrates how to split file operations into modules 
for better maintainability, as requested.

Folder Structure:
file_handling/
├── 0_Manual_File_Handling.py (This file)
├── modules/ (Logic modules)
└── test_file/ (Data files)
"""

from modules import reading, writing, pointer

# Configuration
TEST_FILE = "test_file/manual_example.txt"

print("--- 🚀 Modular File Handling Masterclass ---")

# 1. Writing operations using modules
print("\n[Writing Data]")
writing.write_to_file(TEST_FILE, "Learning modular file handling in Python!\n")
writing.write_multiple_lines(TEST_FILE, [
    "Line 1: Keep code clean.\n",
    "Line 2: Use modules.\n",
    "Line 3: Maintainability is key.\n"
])
print(f"Successfully wrote to {TEST_FILE}")

# 2. Reading operations using modules
print("\n[Reading Data]")
entire_content = reading.read_entire_file(TEST_FILE)
print("Entire File Content:")
print(entire_content)

first_line = reading.read_single_line(TEST_FILE)
print(f"First Line Only: {first_line.strip()}")

part_content = reading.read_by_characters(TEST_FILE, 15)
print(f"First 15 characters: {part_content}")

# 3. Pointer operations using modules
print("\n[Pointer Ops]")
pos = pointer.get_pointer_position(TEST_FILE)
print(f"Initial pointer position: {pos}")

after_offset = pointer.read_from_offset(TEST_FILE, 20)
print(f"Content after seeking to 20:\n{after_offset}")

# 4. Cleanup / Flush
pointer.flush_write(TEST_FILE, "Final state of modular demo.")
print("\nDemo completed. Code is now organized into 'modules' folder.")