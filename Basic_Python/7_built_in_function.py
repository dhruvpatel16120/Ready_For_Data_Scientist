# Built-in Functions in Python

# Using len() to get the length of a string
string_value = "Hello, World!"
length = len(string_value)
print("Length of the string:", length)

# Using type() to get the type of a variable
print("Type of string_value:", type(string_value))

# Using id() to get the memory address of an object
print("ID of string_value:", id(string_value))

# Using sum() to calculate the sum of a list
numbers = [1, 2, 3, 4, 5]
print("Sum of numbers:", sum(numbers))

# Using max() to find the largest number in a list
print("Max of numbers:", max(numbers))

# Using min() to find the smallest number in a list
print("Min of numbers:", min(numbers))

# Using abs() to get the absolute value of a number
negative_number = -10
print("Absolute value:", abs(negative_number))

# Using pow() to calculate power
print("2 to the power of 3:", pow(2, 3))

# Using round() to round a floating-point number
floating_number = 3.14159
print("Rounded value:", round(floating_number, 2))

# Using sorted() to sort a list
unsorted_list = [3, 1, 4, 1, 5, 9]
print("Sorted list:", sorted(unsorted_list))

# Using range() to generate a sequence of numbers
print("Range from 0 to 5:", list(range(6)))

# Using enumerate() to get index and value pairs
print()
for index, value in enumerate(unsorted_list):
    print(f"Index {index}: Value {value}")
print()

# Using zip() to combine two lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print("Zipped list:", list(zip(list1, list2)))

# Using all() to check if all elements are True
bool_list = [True, True, False]
print("All elements True:", all(bool_list))

# Using any() to check if any element is True
print("Any element True:", any(bool_list))

# Using isinstance() to check if an object is of a specific type
print("Is string_value a string?", isinstance(string_value, str))
print()

# Using dir() to list attributes of an object
print("Attributes of string_value:", dir(string_value))
print()

# Using help() to get documentation of an object
print("Help on len function:")
help(len)
print()

# Using reversed() to reverse a sequence
print("Reversed list:", list(reversed(unsorted_list)))

# Using slice( ) to create a slice object
slice_obj = slice(1 , 4)
print("Sliced list:", unsorted_list[slice_obj])

# Using map() to apply a function to all items in an iterable
squared = map(lambda x: x**2, numbers)
print("Squared numbers:", list(squared))

# Using filter() to filter items in an iterable
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print("Even numbers:", list(even_numbers))

# Using eval() to evaluate a string expression
expression = "2 + 3 * 4"
print("Result of eval:", eval(expression))

# Using globals() to get the global symbol table
print()
print("Globals:", globals())
print()

# Using locals() to get the local symbol table
print()
print("Locals:", locals())
print()

a = 10
b = 20
c = 30
print("Binary:",bin(a))
print("octal:",oct(b))
print("hexadecimal:",hex(c))
print()