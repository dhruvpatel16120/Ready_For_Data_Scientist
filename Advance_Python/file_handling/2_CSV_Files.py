# File: 2_CSV_Files.py
# Demonstration of CSV file operations (.csv)
import csv

filename = "Advance_Python/file_handling/data.csv"

# 1. Writing to a CSV file
print("--- Writing to a CSV file ---")
headers = ["ID", "Name", "Subject"]
rows = [
    [1, "Alice", "Python"],
    [2, "Bob", "Java"],
    [3, "Charlie", "C++"]
]

with open(filename, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers) # Writing headers
    writer.writerows(rows)   # Writing multiple data rows
    print(f"Data written to {filename}")

# 2. Reading from a CSV file
print("\n--- Reading from a CSV file ---")
with open(filename, "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"Row Data: {row}")

# 3. Writing CSV using Dictionary (DictWriter)
filename_dict = "Advance_Python/file_handling/data_dict.csv"
print("\n--- Writing CSV using DictWriter ---")
data = [
    {"Name": "Dave", "Age": 25},
    {"Name": "Eve", "Age": 22}
]

with open(filename_dict, "w", newline="") as file:
    fieldnames = ["Name", "Age"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)
    print(f"Dictionary data written to {filename_dict}")

# 4. Reading CSV using Dictionary (DictReader)
print("\n--- Reading CSV using DictReader ---")
with open(filename_dict, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"{row['Name']} is {row['Age']} years old.")
