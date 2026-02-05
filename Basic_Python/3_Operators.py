# Types of Operators:
'''
 Arithmetic operators (+, -, *, /, //, %, **)
 Assignment operators (=, +=, -=, *=)
 Comparison operators (==, !=, >, <, >=, <=)
 Logical operators (and, or, not)
 Bitwise operators (&, |, ^, ~, <<, >>)
 Membership operators (in, not in)
 Identity operators (is, is not)
''' 

# Example of Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("Addition:", a + b)          # Addition
print("Subtraction:", a - b)       # Subtraction
print("Multiplication:", a * b)    # Multiplication
print("Division:", a / b)          # Division
print("Floor Division:", a // b)   # Floor Division
print("Modulus:", a % b)           # Modulus
print("Exponentiation:", a ** b)   # Exponentiation
print()

# Example of Assignment Operators
print("Assignment Operators:")
c = 5
print("Initial value of c:", c)
c += 2
print("After c += 2:", c)
c *= 3
print("After c *= 3:", c)
c -= 4
print("After c -= 4:", c)
c /= 2
print("After c /= 2:", c)
print()

# Example of Comparison Operators
print("Comparison Operators:")
print("a == b:", a == b)           # Equal to
print("a != b:", a != b)           # Not equal to
print("a > b:", a > b)             # Greater than
print("a < b:", a < b)             # Less than
print("a >= b:", a >= b)           # Greater than or equal to
print("a <= b:", a <= b)           # Less than or equal to
print()

# Example of Logical Operators
print("Logical Operators:")
x = True
y = False
print("x and y:", x and y)         # Logical AND
print("x or y:", x or y)           # Logical OR
print("not x:", not x)              # Logical NOT
print()

# Example of Bitwise Operators
print("Bitwise Operators:")
print("a & b:", a & b)             # Bitwise AND 
print("a | b:", a | b)             # Bitwise OR
print("a ^ b:", a ^ b)             # Bitwise XOR
print("~a:", ~a)                   # Bitwise NOT
print("a << 1:", a << 1)           # Left Shift
print("a >> 1:", b >> 1)           # Right Shift
print()

# Example of Membership Operators
print("Membership Operators:")
my_list = [1, 2, 3, 4, 5]
print("3 in my_list:", 3 in my_list)         # Membership test
print("6 not in my_list:", 6 not in my_list) # Membership test
print()

# Example of Identity Operators
print("Identity Operators:")
m = [1, 2, 3]
n = m
o = [1, 2, 3]
print("m is n:", m is n)               # Identity test
print("m is o:", m is o)               # Identity test
print("m is not o:", m is not o)       # Identity test
print()