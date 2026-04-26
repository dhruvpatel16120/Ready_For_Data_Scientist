### list Comprehension (advanced way to create lists)
### Basic list comprehension

# ["expression" for "item" in iterable]
squares = [x**2 for x in range(10)]
square2 = [x * x for x in range(1, 6)]
print("Squares:", squares)
print("Square2:", square2)

# Using functions in List Comprehension
def square_func(x):
    return x * x
squared_numbers = [square_func(x) for x in range(5)]
print("Squared numbers using function:", squared_numbers)

# String Manipulation
names = ["alice", "bob", "charlie", "david"]
upper_names = [name.upper() for name in names]
print("Uppercase Names:", upper_names)

# List comprehension with condition (Filtering)
# ["expression" for "item" in iterable if "condition"]
evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", evens)

# Extracting even numbers and squaring them in one go
complex_result = [x**2 for x in range(10) if x % 2 == 0]
print("Squares of evens:", complex_result)

# Multiple If Conditions
# Numbers between 1-50 that are divisible by 2 and 5
divisible_by_10 = [x for x in range(1, 51) if x % 2 == 0 if x % 5 == 0]
print("Divisible by 2 and 5:", divisible_by_10)


# Filtering with strings
# ['expression' for 'item' in iterable if 'condition']
long_names = [name for name in names if len(name) > 4]
print("Names longer than 4 chars:", long_names)

# Using zip with list comprehension
list1 = [1, 2, 3]
list2 = [10, 20, 30] 
sums = [x + y for x, y in zip(list1, list2)]
print("Sums from zip:", sums)

# Using enumerate
# ['expression' for 'index, value' in enumerate(iterable)]
indexed_list = [f"Index {i}: {val}" for i, val in enumerate(names)]
print("Indexed names:", indexed_list)

# List Comprehension with If–Else (Transformation)
# ["val1" if "condition" else "val2" for "item" in iterable]
result = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
print("Even or Odd:", result)