"""
Python File Modes Deep Dive
===========================

This script demonstrates the various file opening modes in Python.

| Mode | Name | Description | Pointer Position | Overwrites? | Creates File? |
|------|------|-------------|-------------------|------------|---------------|
| 'r'  | Read | Read only(D)| Start             | No         | No (Error)    |
| 'w'  | Write| Write only  | Start             | Yes        | Yes           |
| 'a'  |Append| Append only | End               | No         | Yes           |
| 'r+' | R+W  | Read & Write| Start   | No(unless you write) | No (Error)    |
| 'w+' | W+R  | Write & Read| Start             | Yes        | Yes           |
| 'a+' | A+R  |Append & Read| End               | No         | Yes           |
| 'x'  |Create|Exclusive Create| Start          | No         |Yes(Error if exists)|
| 'b'  |Binary|Binary mode (e.g., 'rb')|    -   |    -       |    -          |
"""

import os

# Helper function to reset demo files
def reset_file(filename, content="Default Content\nLine Two"):
    with open(filename, "w") as f:
        f.write(content)

base_path = "Advance_Python/file_handling/"
demo_file = os.path.join(base_path, "modes_demo.txt")

# --------------------------------------------------------------------------
# 1. READ mode ('r')
# --------------------------------------------------------------------------
print("--- [1] READ MODE ('r') ---")
reset_file(demo_file)
try:
    with open(demo_file, "r") as f:
        print(f"Content: {f.read()}")
        # f.write("Try to write") # This would raise UnsupportedOperation: not writable
except FileNotFoundError:
    print("Error: File not found!")

# --------------------------------------------------------------------------
# 2. WRITE mode ('w')
# --------------------------------------------------------------------------
print("\n--- [2] WRITE MODE ('w') ---")
with open(demo_file, "w") as f:
    f.write("New content overwrites everything.")
with open(demo_file, "r") as f:
    print(f"File now contains: {f.read()}")

# --------------------------------------------------------------------------
# 3. APPEND mode ('a')
# --------------------------------------------------------------------------
print("\n--- [3] APPEND MODE ('a') ---")
with open(demo_file, "a") as f:
    f.write("\nThis line is appended.")
with open(demo_file, "r") as f:
    print(f"File after append: {f.read()}")

# --------------------------------------------------------------------------
# 4. READ+WRITE mode ('r+')
# --------------------------------------------------------------------------
print("\n--- [4] READ+WRITE MODE ('r+') ---")
reset_file(demo_file, "ABCDE")
with open(demo_file, "r+") as f:
    data = f.read(2) # Read "AB"
    print(f"Read 2 chars: {data}")
    f.write("123") # Overwrites from current position (index 2)
    # File content: AB123
with open(demo_file, "r") as f:
    print(f"File after r+ modification: {f.read()}")

# --------------------------------------------------------------------------
# 5. WRITE+READ mode ('w+')
# --------------------------------------------------------------------------
print("\n--- [5] WRITE+READ MODE ('w+') ---")
# w+ overwrites the file IMMEDIATELY on open
with open(demo_file, "w+") as f:
    f.write("Fresh start with w+")
    f.seek(0) # Need to seek back to read what we just wrote
    print(f"Read from w+: {f.read()}")

# --------------------------------------------------------------------------
# 6. APPEND+READ mode ('a+')
# --------------------------------------------------------------------------
print("\n--- [6] APPEND+READ MODE ('a+') ---")
reset_file(demo_file, "Line 1")
with open(demo_file, "a+") as f:
    f.write("\nLine 2")
    f.seek(0) # Pointer was at end, move to start to read
    print(f"Read from a+: \n{f.read()}")

# --------------------------------------------------------------------------
# 7. EXCLUSIVE CREATION ('x')
# --------------------------------------------------------------------------
print("\n--- [7] EXCLUSIVE CREATION ('x') ---")
temp_x = os.path.join(base_path, "exclusive.txt")
if os.path.exists(temp_x):
    os.remove(temp_x)

try:
    with open(temp_x, "x") as f:
        f.write("Only created if file didn't exist.")
    print("File created successfully with 'x'.")
    
    # Second attempt should fail
    with open(temp_x, "x") as f:
        pass
except FileExistsError:
    print("Error: File already exists! 'x' mode protected it.")

# --------------------------------------------------------------------------
# 8. BINARY MODES ('rb', 'wb')
# --------------------------------------------------------------------------
print("\n--- [8] BINARY MODES ('rb', 'wb') ---")
binary_file = os.path.join(base_path, "binary_test.bin")
with open(binary_file, "wb") as f:
    f.write(b"\x00\x01\x02\x48\x65\x6c\x6c\x6f") # Null, 1, 2, "Hello"

with open(binary_file, "rb") as f:
    content = f.read()
    print(f"Binary Content: {content}")

# Cleanup
os.remove(temp_x)
os.remove(binary_file)

print("\n✅ File mode demonstrations complete.")
