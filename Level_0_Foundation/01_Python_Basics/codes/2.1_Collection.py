
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
