import shutil
import os

"""
Python shutil Module
Offers high-level operations on files and collections of files.
"""

# 1. Copying files
source = "source.txt"
destination = "destination.txt"

with open(source, "w") as f:
    f.write("Some content to copy")

shutil.copy(source, destination)
print(f"Copied {source} to {destination}")

# 2. Moving files
shutil.move(destination, "moved_dest.txt")
print("Moved file to moved_dest.txt")

# 3. Archiving (Zip)
# shutil.make_archive("my_archive", 'zip', '.')
# print("Created my_archive.zip")

# 4. Disk usage
usage = shutil.disk_usage(".")
print(f"\nDisk Usage: {usage}")
print(f"Total: {usage.total / (1024**3):.2f} GB")
print(f"Used: {usage.used / (1024**3):.2f} GB")
print(f"Free: {usage.free / (1024**3):.2f} GB")

# 5. Removing directory trees
# shutil.rmtree("folder_to_delete") # CAREFUL: Recursive delete

# Cleaning up
os.remove(source)
os.remove("moved_dest.txt")
