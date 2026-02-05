import json

"""
Python json Module
Enables encoding and decoding data in JSON format.
"""

data = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Physics"],
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}

# 1. Serialization (Python object to JSON string)
json_string = json.dumps(data, indent=4, sort_keys=True)
print("--- JSON String ---")
print(json_string)

# 2. Deserialization (JSON string to Python object)
parsed_data = json.loads(json_string)
print(f"\nParsed Data (dict): {type(parsed_data)}")
print(f"Name: {parsed_data['name']}")

# 3. Working with Files
file_path = "demo_data.json"

# Writing JSON to a file
with open(file_path, "w") as f:
    json.dump(data, f, indent=4)
print(f"\nData written to {file_path}")

# Reading JSON from a file
with open(file_path, "r") as f:
    file_data = json.load(f)
print(f"Data read from file: {file_data['courses']}")

# Cleaning up
import os
os.remove(file_path)
