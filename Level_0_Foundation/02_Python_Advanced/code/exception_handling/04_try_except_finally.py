"""
04: Try-Except-Finally
======================

The 'finally' block executes NO MATTER WHAT happens in the try and except 
blocks. It is most commonly used for cleanup operations like closing 
files or database connections.
"""

import os

filename = "temp_resource.txt"

print("--- [04] Try-Except-Finally Demo ---")

try:
    print(f"Opening {filename}...")
    file = open(filename, "w")
    file.write("Working with resources...")
    
    # Simulate an error
    # x = 1 / 0 

except ZeroDivisionError:
    print("❌ An error occurred (Simulated).")

finally:
    # This runs whether or not an error occurred
    if 'file' in locals() and not file.closed:
        file.close()
        print("🧹 Cleanup: File resource closed safely.")
    
    # Removing temp file for demo purposes
    if os.path.exists(filename):
        os.remove(filename)
        print("🧹 Cleanup: Temporary file deleted.")

print("\nResources are safe.")
