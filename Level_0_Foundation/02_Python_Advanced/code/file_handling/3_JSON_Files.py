# File: 3_JSON_Files.py
# Demonstration of JSON file operations (.json)
import json

filename = "Level_0_Foundation/02_Python_Advanced/code/file_handling/test_file/user_data.json"

# Python dictionary to be saved as JSON
user_info = {
    "name": "John Doe",
    "age": 30,
    "skills": ["Python", "Machine Learning", "Cloud"],
    "is_student": False
} 

# 1. Writing to a JSON file
print("--- Writing to a JSON file ---")
with open(filename, "w") as file:
    # json.dump converts dictionary to JSON and saves to file
    json.dump(user_info, file) 
    print(f"Data saved to {filename}")

# 2. Reading from a JSON file
print("\n--- Reading from a JSON file ---")
with open(filename, "r") as file:
    # json.load reads JSON from file and converts back to dictionary
    loaded_data = json.load(file)
    print("Loaded Data:", loaded_data)
    print(f"Name: {loaded_data['name']}")

# 3. Converting to JSON string (Serialization)
print("\n--- JSON Serialization (Dict to String) ---")
json_string = json.dumps(user_info)
print(f"JSON String: {json_string}")

# 4. Converting from JSON string (Deserialization)
print("\n--- JSON Deserialization (String to Dict) ---")
parsed_dict = json.loads(json_string)
print(f"Parsed Dictionary: {parsed_dict}")
