import bisect

"""
Python bisect Module
Support for maintaining a list in sorted order without having to sort the list after each insertion.
"""

# sorted list
data = [1, 2, 4, 4, 5, 8, 9]

print(f"Sorted data: {data}")

# 1. bisect_left and bisect_right (finding insertion points)
# Returns the index where 'x' should be inserted to maintain order
x = 4
pos_left = bisect.bisect_left(data, x)
pos_right = bisect.bisect_right(data, x)

print(f"Index to insert {x} (left): {pos_left}")
print(f"Index to insert {x} (right): {pos_right}")

# 2. insort
# Actually inserts the item into the list
bisect.insort(data, 6)
print(f"Data after insort(6): {data}")

# 3. Use case: Grade lookup
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

scores = [33, 99, 77, 70, 89, 90, 100]
print("\nGrade Lookup:")
for s in scores:
    print(f"Score {s} -> Grade {grade(s)}")
