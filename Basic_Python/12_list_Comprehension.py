# list Comprehension (advanced way to create lists)

# Basic list comprehension
# ["expression" for "item" in iterable]
squares = [x**2 for x in range(10)]
square2 = [x * x for x in range(1, 6)]
print("Squares:", squares)
print("Square2:", square2)

# List comprehension with condition (Filtering)
# ["expression" for "item" in iterable if "condition"]
evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", evens)

# List Comprehension with If–Else (Transformation)
# ["val1" if "condition" else "val2" for "item" in iterable]
result = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print("Even or Odd:", result)

# Nested List Comprehension (Matrix creation)
# [["expression" for "j" in inner] for "i" in outer]
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print("Matrix:")
for row in matrix:
    print(row)

# Flattening a nested list (Multiple for loops)
# ["item" for "sublist" in outer_list for "item" in sublist]
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flattened)

# Using functions in List Comprehension
def square_func(x):
    return x * x
squared_numbers = [square_func(x) for x in range(5)]
print("Squared numbers using function:", squared_numbers)

# --- NEW EXAMPLES ---

# String Manipulation
names = ["alice", "bob", "charlie", "david"]
upper_names = [name.upper() for name in names]
print("Uppercase Names:", upper_names)

# Filtering with strings
long_names = [name for name in names if len(name) > 4]
print("Names longer than 4 chars:", long_names)

# Multiple If Conditions
# Numbers between 1-50 that are divisible by 2 and 5
divisible_by_10 = [x for x in range(1, 51) if x % 2 == 0 if x % 5 == 0]
print("Divisible by 2 and 5:", divisible_by_10)

# Nested Loops with Filtering
# All pairs (x, y) where x is from [1,2] and y is from [3,4] but x != y
pairs = [(x, y) for x in range(1, 3) for y in range(3, 5) if x != y]
print("Pairs:", pairs)

# Using zip with list comprehension
list1 = [1, 2, 3]
list2 = [10, 20, 30] 
sums = [x + y for x, y in zip(list1, list2)]
print("Sums from zip:", sums)

# Using enumerate
indexed_list = [f"Index {i}: {val}" for i, val in enumerate(names)]
print("Indexed names:", indexed_list)

# Extracting even numbers and squaring them in one go
complex_result = [x**2 for x in range(10) if x % 2 == 0]
print("Squares of evens:", complex_result)

# Flattening and filtering simultaneously
# Get all numbers > 5 from a nested list
filtered_flattened = [item for sublist in nested_list for item in sublist if item > 5]
print("Flattened and filtered (>5):", filtered_flattened)

# Creating a list of dictionaries (List comprehension can create objects)
people = [{"name": name, "len": len(name)} for name in names]
print("List of dicts:", people)


