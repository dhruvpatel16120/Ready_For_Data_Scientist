# 02_Else_Finally.py
# Level: 🟡 Intermediate
# Topic: The complete block - Try, Except, Else, and Finally

"""
- try: The risky code
- except: Runs only if an error occurs
- else: Runs only if NO error occurs
- finally: Runs NO MATTER WHAT (Cleanup code)
"""

print("--- Try-Except-Else-Finally ---")

try:
    file_path = "Advance_Python/exception_handling/test.txt"
    file = open(file_path, "w")
    data = input("Enter something to write to file: ")
    file.write(data)
    print("Writing successful.")

except IOError:
    print("❌ Error: Could not write to file.")

else:
    # This only runs if the 'try' block was successful
    print("✅ No errors occurred during file operation.")

finally:
    # This is usually used for closing files or database connections
    if 'file' in locals():
        file.close()
    print("🧹 Cleanup: File connection closed.")
