# list Comprehension (advanced way to create lists)

# Basic list comprehension

# Create a list of squares of numbers from 0 to 9
squares = [x**2 for x in range(10)]
# ["expression or work " for "item or variable" in iterable]

print("Squares:", squares)

# List comprehension with condition

# Create a list of even numbers from 0 to 9
evens = [x for x in range(10) if x % 2 == 0]
# ["expression or work " for "item or variable" in iterable if "condition"]
print("Even numbers:", evens)


# List Comprehension with If–Else
result = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
# ["expression1" if "condition" else "expression2" for "item or variable" in iterable]
print("Even or Odd:", result)

# Nested List Comprehension
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
# [["expression or work " for "item or variable" in iterable] for "item or variable" in iterable]
print("Matrix:")
for row in matrix:
    print(row)

# Flattening a nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flattened)

# Using functions in List Comprehension
def square(x):
    return x * x
squared_numbers = [square(x) for x in range(5)]
print("Squared numbers using function:", squared_numbers)
