# Define Data Types of python

# core Data Types in Python
a = 10           # Integer
b = 3.14         # Float
c = 1+2j         # Complex Number

d = "Hello"      # String 1
e = 'World'      # String 2
f = '''Python''' # String 3

g = True         # Boolean
h = None         # NoneType

# Simple assignment example
name = "Alice"
age = 25

# Multiple assignment example
x, y, z = 10, 20, 30

## Same value to multiple variables
# a = b = c = 0 # it gives same memory address

# print memory address of variables
print(id(a))
# print(id(b))
# print(id(c))
# print(id(x))
# print(id(y))
# print(id(z))

## Displaying the data types
print("Data type of a (10) is:", type(a))
# print("Data type of b (3.14) is:", type(b))
# print("Data type of c (1+2j) is:", type(c))
# print("Data type of d (Hello) is:", type(d))
# print("Data type of e ('World') is:", type(e))
# print("Data type of f ('''Python''') is:", type(f))
# print("Data type of g (True) is:", type(g))
# print("Data type of h (None) is:", type(h))

## check instance type of variables
print("instance type of b (3.14) is:", isinstance(b, float))
# print("instance type of b (3.14) is:", isinstance(b, int))
