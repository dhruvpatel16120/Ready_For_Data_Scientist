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

# Simple assignment
name = "Alice"
age = 25

# Multiple assignment
x, y, z = 10, 20, 30

## Same value to multiple variables
# a = b = c = 0 # it gives same memory address

# print(id(a))
# print(id(b))
# print(id(c))
# print(id(x))
# print(id(y))
# print(id(z))

## Displaying the data types
# print("Data type of a (10) is:", type(a))
# print("Data type of b (3.14) is:", type(b))
# print("Data type of c (1+2j) is:", type(c))
# print("Data type of d (Hello) is:", type(d))
# print("Data type of e ('World') is:", type(e))
# print("Data type of f ('''Python''') is:", type(f))
# print("Data type of g (True) is:", type(g))
# print("Data type of h (None) is:", type(h))

## check instance type of variables
# print("instance type of b (3.14) is:", isinstance(b, float))
# print("instance type of b (3.14) is:", isinstance(b, int))

# collection Data Types in Python

list_example = [1, 2, 3, 4, 5]               # List
tuple_example = (1, 2, 3, 4, 5)              # Tuple
set_example = {1, 2, 3, 4, 5}                # Set
dict_example = {'a': 1, 'b': 2, 'c': 3}      # Dictionary
range_example = range(1, 10)                 # Range
byte_example = b'Hello'                      # Bytes
bytes_example = bytes(5)                     # Bytes it returns b'\x00\x00\x00\x00\x00'
bytes_example2 = bytes([65, 66, 67, 68, 69])    # Bytes it returns b'ABCDE'
bytearray_example = bytearray(5)             # Bytearray
memoryview_example = memoryview(bytearray(5))  # Memoryview
frozenset_example = frozenset([1, 2, 3, 4, 5]) # Frozenset it is immutable version of set we cannot change it after creation

## frozenset example
# frozenset_example = frozenset_example + {6} # it will give error because it is immutable

# Displaying the collection data types
print("Data type of list_example is:", type(list_example))
print("Data type of range_example is:", type(range_example))
print("Data type of frozenset_example is:", type(frozenset_example))
print("Data type of byte_example is:", type(byte_example))
print("Data type of bytes_example is:", type(bytes_example))
print("Data type of memoryview_example is:", type(memoryview_example))
print("Data type of bytearray_example is:", type(bytearray_example))

# displaying values :
print("value of byte_example is:", byte_example)
print("value of bytes_example is:", bytes_example)
print("value of bytes_example2 is:", bytes_example2)
print("value of bytearray_example is:", bytearray_example)
print("value of memoryview_example is:", memoryview_example)
print("value of frozenset_example is:", frozenset_example)

## example of global and nonlocal variables and nonlocal keyword
global_var = 10

def example_function():
    local_var = 20
    nonlocal global_var # it creates a reference to the global variable
    global_var = 20
    print("Local variable:", local_var)
    print("Global variable:", global_var)

example_function()
# print("local variable outside the function:", local_var) # it will give error because local variable is not accessible outside the function
print("Global variable outside the function:", global_var)
# print("nonlocal variable outside the function:", nonlocal global_var) # it will give error because nonlocal variable is not accessible outside the function 