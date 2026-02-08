"""
File Pointer Operations: seek(), tell(), and flush()
===================================================

This script demonstrates how to control and track the file pointer (cursor)
using seek() and tell(), and how to force write operations using flush().

1. tell(): Returns the current position of the file pointer.
2. seek(offset, from_what): Moves the file pointer to a new position.
   - offset: Number of bytes to move.
   - from_what: 0 (start), 1 (current), 2 (end). Reference point.
3. flush(): Forces the buffer to write data to the disk without closing the file.
"""

import os

filename = "Advance_Python/file_handling/pointer_demo.txt"

# --------------------------------------------------------------------------
# 1. Using seek() and tell() with Read Mode ('r')
# --------------------------------------------------------------------------
print("--- [1] seek() and tell() in READ mode ---")
# Create the file first
with open(filename, "w") as f:
    f.write("A-B-C-D-E-F-G-H-I-J")

with open(filename, "r") as f:
    print(f"Initial pointer position: {f.tell()}")
    
    data = f.read(3)
    print(f"Read 3 chars: '{data}'")
    print(f"Pointer now at: {f.tell()}")
    
    # Move pointer back to the beginning
    f.seek(0)
    print(f"seek(0) moved pointer back to: {f.tell()}")
    print(f"Read again: '{f.read(3)}'")
    
    # Move pointer to character at index 4
    f.seek(4)
    print(f"seek(4) moved pointer to: {f.tell()}")
    print(f"Character at index 4: '{f.read(1)}'")

# --------------------------------------------------------------------------
# 2. Using tell() and flush() with Write Mode ('w')
# --------------------------------------------------------------------------
print("\n--- [2] tell() and flush() in WRITE mode ---")
with open(filename, "w") as f:
    print(f"Initial write position: {f.tell()}")
    f.write("Line One\n")
    print(f"Position after writing 'Line One': {f.tell()}")
    
    f.write("Line Two")
    print("Forcing write to disk using flush()...")
    f.flush() # Data is now safely on disk even if script crashes before close()
    
    # Note: In 'w' mode, seek() can overwrite specific parts of the file
    # but it's often tricky with variable length encodings (UTF-8).
    f.seek(0)
    f.write("HEAD") # Overwrites "Line" with "HEAD"
    print("Overwrote first 4 bytes with 'HEAD'.")

# Verify the overwrite
with open(filename, "r") as f:
    print(f"File content after overwrite: {f.read()}")

# --------------------------------------------------------------------------
# 3. Using seek() and tell() with Append Mode ('a')
# --------------------------------------------------------------------------
print("\n--- [3] seek() and tell() in APPEND mode ---")
with open(filename, "a") as f:
    print(f"Initial position in append mode: {f.tell()} (Should be at the end)")
    
    # IMPORANT: In append mode, the pointer is moved to the end
    # BEFORE every write, regardless of where you seek to.
    f.seek(0)
    print(f"Attempted seek(0), pointer at: {f.tell()}")
    f.write(" - Appended Line") 
    print("Performed f.write(). In 'a' mode, it always appends to the end.")

with open(filename, "r") as f:
    print(f"Final file content: {f.read()}")

# --------------------------------------------------------------------------
# 4. Binary Mode (Necessary for relative seeks from CURRENT or END)
# --------------------------------------------------------------------------
print("\n--- [4] Multiple seek references (Binary Mode) ---")
# Standard text files only allow seeking from the START (0) 
# unless the offset is 0. For relative seeks, use binary mode 'rb'.

with open(filename, "rb") as f:
    f.seek(5) # Start at index 5
    print(f"Start at 5: {f.tell()}")
    
    f.seek(2, 1) # Move 2 bytes forward from CURRENT position
    print(f"Move +2 from current: {f.tell()}")
    
    f.seek(-3, 2) # Move 3 bytes backward from END
    print(f"Move -3 from end: {f.tell()}")
    print(f"Read last 3 bytes: {f.read().decode()}")

# Cleanup
if os.path.exists(filename):
    # os.remove(filename) # Uncomment to delete the demo file
    pass

print("\n✅ File pointer demonstrations complete.")
