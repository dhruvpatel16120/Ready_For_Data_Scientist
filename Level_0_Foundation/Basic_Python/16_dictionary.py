# Dictionary Methods Demonstration Program

print("----- DICTIONARY CREATION -----")

student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

print("Initial Dictionary:", student)

print("\n----- ACCESSING ELEMENTS -----")

# Access using key
print("Name:", student["name"]) # if key not found it will throw error

# Access using get() safe method
print("Age:", student.get("age"))
print("Marks (safe access):", student.get("marks", "Not Found"))

print("\n----- ADDING & UPDATING ELEMENTS -----")

# Add new key-value pair
student["city"] = "Delhi"
print("After adding city:", student)

# Update existing value
student["age"] = 21
print("After updating age:", student)

# update() method
student.update({"marks": 90, "grade": "A+"})
print("After update():", student)

print("\n----- DICTIONARY METHODS -----")

# keys()
print("Keys:", student.keys())

# values()
print("Values:", student.values())

# items()
print("Items:", student.items())

print("\n----- REMOVING ELEMENTS -----")

# pop()
removed_value = student.pop("marks")
print("After pop('marks'):", student)
print("Removed value:", removed_value)

# popitem()
removed_item = student.popitem()
print("After popitem():", student)
print("Removed item:", removed_item)

print("\n----- SETDEFAULT METHOD -----")

# setdefault() :- retun the value of the key if key is present otherwise return the default value
student.setdefault("country", "India")
print("After setdefault('country'):", student)

# setdefault() when key exists
student.setdefault("name", "Bob") 
print("After setdefault('name'):", student)

print("\n----- COPYING DICTIONARY -----")

# copy()
student_copy = student.copy()
print("Copied dictionary:", student_copy)

print("\n----- ITERATING THROUGH DICTIONARY -----")

# Loop through keys
print("Keys:")
for key in student:
    print(key)

# Loop through values
print("\nValues:")
for value in student.values():
    print(value)

# Loop through key-value pairs
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)

print("\n----- NESTED DICTIONARY -----")

students = {
    1: {"name": "Alice", "age": 20},
    2: {"name": "Bob", "age": 22}
}

print("Nested Dictionary:", students)
print("Student 1 Name:", students[1]["name"])

print("\n----- DICTIONARY COMPREHENSION -----")

# Dictionary comprehension
squares = {x: x*x for x in range(1, 6)}
# {"key_expression": "value_expression" for "item or variable" in iterable}
print("Squares Dictionary:", squares)

print("\n----- CLEAR DICTIONARY -----")

temp = {"a": 1, "b": 2}
temp.clear()
print("After clear():", temp)

print("\n----- MEMBERSHIP TEST -----")

print("'name' in student:", "name" in student)
print("'salary' not in student:", "salary" not in student)
