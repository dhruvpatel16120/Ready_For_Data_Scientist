# tuple in python

# tuple creatation
tuple_a = (1,2,3,4)

# Normal Tuple
t = (1, 2, 3)
# Single-Element Tuple (Important)
t2 = (10,)   # comma is mandatory
# Without comma:
t3 = (10)    # NOT a tuple

# Tuple elements cannot be modified.
#  t[0] = 100   # Error

# However, if a tuple contains a mutable object:
t = (1, [2, 3])
t[1][0] = 10   # Allowed
nested = (1, (2, 3), (4, 5))

# Tuple Packing and Unpacking
point = (10, 20)  # Packing
x, y = point      # Unpacking


print("Tuple a:", tuple_a)
print("Tuple t:", t)
print("Type of t:", type(t))
print("Single-element Tuple t2:", t2)
print("Type of t2:", type(t2))
print("Not a tuple t3:", t3)
print("Type of t3:", type(t3))
print("Modified nested tuple t:", t)
print("Nested tuple:", nested)
print("Packed point:", point)
print("Unpacked x:", x)
print("Unpacked y:", y)
print("Type of point:", type(point))

# tuple methods demonstration
tuple_b = (5, 10, 15, 10, 20)
print("Tuple b:", tuple_b)

# count() – count occurrences of a value
print("Count of 10 in tuple_b:", tuple_b.count(10))

# index() – find index of first occurrence of a value
print("Index of 15 in tuple_b:", tuple_b.index(15))

# length of tuple
print("Length of tuple_b:", len(tuple_b))

# concatenation
tuple_c = tuple_a + tuple_b
print("Concatenated tuple (a + b):", tuple_c)

# Add element in Tuple 
# Method 1: Tuple concatenation (most common)

t = (1, 2, 3)
t = t + (4,)
print(t)
# Output:(1, 2, 3, 4)

# Important detail
# (4,) is a single-element tuple. The comma is required. Without it:
# (4) This is just an integer, not a tuple

# Method 2: Using unpacking (*) — cleaner style
t = (1, 2, 3)
t = (*t, 4)
t = (0, *t)
print(t)
# This unpacks all elements of t and adds 4 at the end.
# You can also add at the beginning: t = (0, *t)

# Method 3: Convert to list and back (for multiple edits)
t = (1, 2, 3)
temp = list(t)
temp.append(4)
t = tuple(temp)
