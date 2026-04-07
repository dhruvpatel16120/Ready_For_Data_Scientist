# Type Casting in Python

# Implicit Type Casting
x = 5           # Integer
y = 2.0         # Float
z = x + y      # Implicitly converts x to float and adds
# print("Implicit Type Casting:")
# print("x (int):", x)
# print("y (float):", y)
# print("z (x + y):", z)
# print("Type of z:", type(z))
# print()

# Explicit Type Casting
a="10"        # String
b=5           # Integer
c=float(b)    # Explicitly converts b to float
d=int(a)      # Explicitly converts a to integer
e=str(b)      # Explicitly converts b to string
f=bool(b)     # Explicitly converts b to boolean
# print("Explicit Type Casting:")
# print("a (string):", a)
# print("b (int):", b)
# print("c (float of b):", c)
# print("d (int of a):", d)
# print("e (string of b):", e)
# print("f (boolean of b):", f)
# print("Type of c:", type(c))
# print("Type of d:", type(d))
# print("Type of e:", type(e))
# print("Type of f:", type(f))
# print()

# convert string to list
str_value = "Hello"
list_value = list(str_value)  # Explicitly converts string to list
# print("String to List Conversion:")
# print("str_value (string):", str_value)
# print("list_value (list):", list_value)
# print("Type of list_value:", type(list_value))
# print()

# convert list to string
chars = ['P', 'y', 't', 'h', 'o', 'n']
text = "".join(chars)
# print("List to String Conversion:")
# print("chars (list):", chars)
# print("text (string):", text)
# print("Type of text:", type(text))
# print()

# Type casting for Collection Data Types
print("Collection Type Casting:")

# List to Tuple
list_example = [1, 2, 3, 4, 5]
tuple_example = tuple(list_example)  # Converts list to tuple
# print("List to Tuple:")
# print("list_example (list):", list_example)
# print("tuple_example (tuple):", tuple_example)
# print("Type of tuple_example:", type(tuple_example))
# print()

# Tuple to Set
tuple_example2 = (1, 2, 2, 3, 4)
set_example = set(tuple_example2)  # Converts tuple to set
# print("Tuple to Set:")
# print("tuple_example2 (tuple):", tuple_example2)
# print("set_example (set):", set_example)
# print("Type of set_example:", type(set_example))
# print()

# Set to List
set_example2 = {1, 2, 3, 4, 5}
list_example2 = list(set_example2)  # Converts set to list
# print("Set to List:")
# print("set_example2 (set):", set_example2)
# print("list_example2 (list):", list_example2)
# print("Type of list_example2:", type(list_example2))
# print()

# Dictionary to List of Keys
dict_example = {'a': 1, 'b': 2, 'c': 3}
list_of_keys = list(dict_example)  # Converts dictionary to list of keys
list_of_values = list(dict_example.values())  # Converts dictionary to list of values
list_of_items = list(dict_example.items())  # Converts dictionary to list of items
# print("Dictionary to List of Keys:")
# print("dict_example (dict):", dict_example)
# print("list_of_keys (list):", list_of_keys)
# print("Type of list_of_keys:", type(list_of_keys))
# print("list_of_values (list):", list_of_values)
# print("Type of list_of_values:", type(list_of_values))
# print("list_of_items (list):", list_of_items)
# print("Type of list_of_items:", type(list_of_items))
# print()

# List to Dictionary 
list_example3 = [('a', 1), ('b', 2), ('c', 3)]
dict_from_list = dict(list_example3)  # Converts list of tuples to dictionary
print("List to Dictionary:")
print("list_example3 (list of tuples):", list_example3)
print("dict_from_list (dict):", dict_from_list)
print("Type of dict_from_list:", type(dict_from_list))
print()

# set to dictionary
set_example3 = {('a', 1), ('b', 2), ('c', 3)}
dict_from_set = dict(set_example3)  # Converts set of tuples to dictionary
print("Set to Dictionary:")
print("set_example3 (set of tuples):", set_example3)
print("dict_from_set (dict):", dict_from_set)
print("Type of dict_from_set:", type(dict_from_set))
print()

# set to frozenset
set_example4 = {1, 2, 3, 4, 5}
frozenset_example2 = frozenset(set_example4)  # Converts set to frozenset and make it immutable
print("Set to Frozenset:")
print("set_example4 (set):", set_example4)
print("frozenset_example2 (frozenset):", frozenset_example2)
print("Type of frozenset_example2:", type(frozenset_example2))
print()


# Example of Type Casting with user input

# Converting user input (string) to integer
# user_input = input("Enter a number: ")  # Input is string
# user_number = int(user_input)            # Explicitly convert to integer
# print("You entered number:", user_number)
# print("Type of user_number:", type(user_number))
# print()

# Converting user input (string) to integer
# user_input2 = input("Enter a number: ")  # Input is string
# user_number2 = float(user_input2)            # Explicitly convert to integer
# print("You entered number:", user_number2)
# print("Type of user_number2:", type(user_number2))
# print()
