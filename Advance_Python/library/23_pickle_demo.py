import pickle
import os

"""
Python pickle Module
Implements binary protocols for serializing and de-serializing a Python object structure.
"""

data = {
    "numbers": [1, 2, 3],
    "string": "Hello Pickle",
    "nested": {"a": 1, "b": 2},
    "set": {10, 20}
}

file_path = "data.pkl"

# 1. Pickling (Serialization)
print(f"--- Pickling data to {file_path} ---")
with open(file_path, "wb") as f:
    pickle.dump(data, f)

# 2. Unpickling (Deserialization)
print("\n--- Unpickling data ---")
with open(file_path, "rb") as f:
    loaded_data = pickle.load(f)

print(f"Loaded data type: {type(loaded_data)}")
print(f"Set: {loaded_data['set']}")
print(f"Matches original: {loaded_data == data}")

# 3. Pickling custom classes
class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
pickled_p = pickle.dumps(p1) # Serialize to bytes string
unpickled_p = pickle.loads(pickled_p)
print(f"\nUnpickled person name: {unpickled_p.name}")

# Cleaning up
os.remove(file_path)
