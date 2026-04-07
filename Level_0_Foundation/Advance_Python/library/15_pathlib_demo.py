from pathlib import Path

"""
Python pathlib Module
Offers classes representing filesystem paths with semantics appropriate for different operating systems.
Object-oriented alternative to os.path.
"""

# 1. Creating Path objects
p = Path('.')
print(f"Current Path: {p.resolve()}")

# 2. Joining paths using / operator
new_file = p / "subdir" / "my_file.txt"
print(f"Joined Path: {new_file}")

# 3. Path Properties
print(f"Name: {new_file.name}")
print(f"Suffix: {new_file.suffix}")
print(f"Stem: {new_file.stem}")
print(f"Parent: {new_file.parent}")
print(f"Is Absolute? {new_file.is_absolute()}")

# 4. Filesystem operations
temp_file = Path("hello.txt")
temp_file.write_text("Hello from pathlib!") # Create and write
print(f"\nFile content: {temp_file.read_text()}")
print(f"File exists? {temp_file.exists()}")

# 5. Iterating over directories
print("\nIterating over directory:")
for file in Path('.').iterdir():
    if file.is_file():
        print(f" - {file.name}")

# Cleaning up
temp_file.unlink() # Delete file
