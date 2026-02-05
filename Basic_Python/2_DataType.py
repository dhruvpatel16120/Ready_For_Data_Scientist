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

# Displaying the data types
print("Data type of a (10) is:", type(a))

# check instance type of variables
print("instance type of b (3.14) is:", isinstance(b, float))
print("instance type of b (3.14) is:", isinstance(b, int))

# collection Data Types in Python

list_example = [1, 2, 3, 4, 5]               # List
tuple_example = (1, 2, 3, 4, 5)              # Tuple
set_example = {1, 2, 3, 4, 5}                # Set
dict_example = {'a': 1, 'b': 2, 'c': 3}      # Dictionary
range_example = range(1, 10)                 # Range
byte_example = b'Hello'                      # Bytes
bytearray_example = bytearray(5)             # Bytearray
memoryview_example = memoryview(bytearray(5))  # Memoryview
frozenset_example = frozenset([1, 2, 3, 4, 5]) # Frozenset

# Displaying the collection data types
print("Data type of list_example is:", type(list_example))
print("Data type of range_example is:", type(range_example))
print("Data type of frozenset_example is:", type(frozenset_example))
print("Data type of byte_example is:", type(byte_example))
print("Data type of memoryview_example is:", type(memoryview_example))
print("Data type of bytearray_example is:", type(bytearray_example))

# displaying values :
print("value of byte_example is:", byte_example)
print("value of bytearray_example is:", bytearray_example)
print("value of memoryview_example is:", memoryview_example)
print("value of frozenset_example is:", frozenset_example)