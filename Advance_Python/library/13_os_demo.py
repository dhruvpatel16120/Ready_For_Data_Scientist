import os

"""
Python os Module
This module provides a portable way of using operating system dependent functionality.
"""

# 1. Getting current configuration
print(f"Current Working Directory: {os.getcwd()}")
print(f"OS Name: {os.name}") # 'posix', 'nt', 'java'
# print(f"Environment Variables: {os.environ}")

# 2. Directory Operations
dir_name = "test_dir"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
    print(f"\nCreated directory: {dir_name}")

print(f"Contents of current directory: {os.listdir('.')[:5]}...") # List first 5 items

# 3. Path manipulations (os.path)
file_path = os.path.join(os.getcwd(), "test.txt")
print(f"\nJoined Path: {file_path}")
print(f"Is absolute? {os.path.isabs(file_path)}")
print(f"Basename: {os.path.basename(file_path)}")
print(f"Dirname: {os.path.dirname(file_path)}")
print(f"Split path: {os.path.split(file_path)}")
print(f"Extension: {os.path.splitext(file_path)[1]}")

# 4. Process-related
print(f"\nProcess ID: {os.getpid()}")

# Cleaning up
if os.path.exists(dir_name):
    os.rmdir(dir_name)
    print(f"Removed directory: {dir_name}")
