import csv
import os

"""
Python csv Module
Implements classes to read and write tabular data in CSV format.
"""

file_path = "data.csv"
data = [
    ["Name", "Age", "City"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "Los Angeles"],
    ["Charlie", 35, "Chicago"]
]

# 1. Writing to CSV
print(f"--- Writing to {file_path} ---")
with open(file_path, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)

# 2. Reading from CSV
print("\n--- Reading from CSV ---")
with open(file_path, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# 3. DictReader and DictWriter (Preferred for named columns)
dict_data = [
    {"Name": "Dave", "Age": 40, "City": "Boston"},
    {"Name": "Eve", "Age": 28, "City": "Seattle"}
]

print("\n--- Using DictWriter ---")
with open(file_path, "a", newline='') as f:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    # writer.writeheader() # Already written by writerows above in this demo
    writer.writerows(dict_data)

print("\n--- Using DictReader ---")
with open(file_path, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['Name']} lives in {row['City']}")

# Cleaning up
os.remove(file_path)
