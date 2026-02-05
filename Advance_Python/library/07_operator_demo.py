import operator

"""
Python operator Module
Exports a set of efficient functions corresponding to the intrinsic operators of Python.
"""

a, b = 10, 5

print(f"a = {a}, b = {b}")
print(f"add(a, b): {operator.add(a, b)}")
print(f"sub(a, b): {operator.sub(a, b)}")
print(f"mul(a, b): {operator.mul(a, b)}")
print(f"truediv(a, b): {operator.truediv(a, b)}")
print(f"floordiv(a, b): {operator.floordiv(a, b)}")
print(f"mod(a, b): {operator.mod(a, b)}")
print(f"pow(a, b): {operator.pow(a, b)}")

print("\n--- Comparison ---")
print(f"lt(a, b): {operator.lt(a, b)}") # a < b
print(f"le(a, b): {operator.le(a, b)}") # a <= b
print(f"eq(a, b): {operator.eq(a, b)}") # a == b
print(f"ne(a, b): {operator.ne(a, b)}") # a != b
print(f"gt(a, b): {operator.gt(a, b)}") # a > b
print(f"ge(a, b): {operator.ge(a, b)}") # a >= b

print("\n--- Item/Attribute Accessors ---")
data = [('apple', 3), ('banana', 1), ('cherry', 2)]

# Using itemgetter to sort by price (index 1)
data.sort(key=operator.itemgetter(1))
print(f"Sorted by index 1: {data}")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("Alice", 30), Person("Bob", 20), Person("Charlie", 25)]
# Using attrgetter to sort by age
people.sort(key=operator.attrgetter('age'))
print(f"Sorted by age: {[p.name for p in people]}")

print("\n--- Logical ---")
print(f"not_(True): {operator.not_(True)}")
print(f"truth([1]): {operator.truth([1])}")
