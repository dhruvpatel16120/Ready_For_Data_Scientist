# Complete Set Demonstration Program in Python

print("----- SET CREATION -----")

# Creating sets
A = {1, 2, 3, 4}
B = set([3, 4, 5, 6])
print("Set A:", A)
print("Set B:", B)

# Empty set
empty_set = set()
print("Empty Set:", empty_set)

print("\n----- UNIQUENESS PROPERTY -----")
duplicates = {1, 2, 2, 3, 3, 4}
print("set with duplicates: duplicates = {1, 2, 2, 3, 3, 4}")
print("Duplicates removed automatically:", duplicates)

print("\n----- ADDING ELEMENTS -----")
A.add(10)
print("After add(10):", A)

A.update([20, 30])
print("After update([20, 30]):", A)

print("\n----- REMOVING ELEMENTS -----")
A.remove(10)
print("After remove(10):", A)

A.discard(100)  # No error if element not present
print("After discard(100):", A)

removed_item = A.pop()
print("After pop():", A)
print("Removed item:", removed_item)

print("\n----- ITERATING OVER SET -----")
for item in A:
    print(item, end=" ")
print()

print("\n----- SET OPERATIONS -----")
print("Union (A | B):", A | B)
print("Intersection (A & B):", A & B)
print("Difference (A - B):", A - B)
print("Symmetric Difference (A ^ B):", A ^ B)

print("\n----- SET METHODS -----")
print("A union B:", A.union(B))
print("A intersection B:", A.intersection(B))
print("A difference B:", A.difference(B))
print("A symmetric_difference B:", A.symmetric_difference(B))

print("\n----- SET COMPARISON METHODS -----")
C = {1, 2}
print("C is subset of A:", C.issubset(A))
print("A is superset of C:", A.issuperset(C))
print("A is disjoint with B:", A.isdisjoint(B))

print("\n----- CLEAR METHOD -----")
temp = {1, 2, 3}
temp.clear()
print("After clear():", temp)

print("\n----- FROZENSET -----")
fs = frozenset([1, 2, 3])
print("Frozenset:", fs)
print("Type of fs:", type(fs))

print("\n----- MEMBERSHIP TEST -----")
print("2 in A:", 2 in A)
print("50 not in A:", 50 not in A)
