# User Define Function

# Function to add two numbers
def add(a, b):
    return a + b

# 1. No arguments, no return value
def greet():
    print("Hello")

# 2. Arguments, no return value
def greet(name):
    print("Hello", name)

# 3. No arguments, return value
def get_pi():
    return 3.14

# 4. Arguments and return value
def square(x):
    return x * x

# Positional Arguments
def add(a, b):
    return a + b

# Default Arguments
def greet(name="User"):
    print(name)

# Variable-Length Arguments
def total(*nums):
    return sum(nums)

# function call
print("Addition:", add(5, 3))
greet(name="Alice")
greet("Bob")
print("Value of Pi:", get_pi())
print("Square of 4:", square(4))
print("Total:", total(1, 2, 3, 4, 5))
