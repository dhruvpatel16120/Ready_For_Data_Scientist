import itertools

"""
Python itertools Module
Functions creating iterators for efficient looping.
"""

print("--- Infinite Iterators ---")
# count(start, step)
counter = itertools.count(10, 2)
print(f"count: { [next(counter) for _ in range(5)] }")

# cycle(iterable)
cycler = itertools.cycle('ABC')
print(f"cycle: {[next(cycler) for _ in range(7)]}")

# repeat(object, times)
repeater = itertools.repeat(10, 3)
print(f"repeat: {list(repeater)}")

print("\n--- Combinatoric Iterators ---")
items = 'ABC'

# product() - Cartesian product
print(f"product('AB', '12'): { list(itertools.product('AB', '12')) }")

# permutations()
print(f"permutations('ABC', 2): { list(itertools.permutations(items, 2)) }")

# combinations()
print(f"combinations('ABC', 2): {list(itertools.combinations(items, 2))}")

# combinations_with_replacement()
print(f"combinations_with_replacement('ABC', 2): {list(itertools.combinations_with_replacement(items, 2))}")

print("\n--- Iterators terminating on the shortest input sequence ---")
# chain()
print(f"chain([1,2], [3,4]): {list(itertools.chain([1,2], [3,4], [5,6], [7,8]))}")

# compress()
print(f"compress('ABCDE', [1,0,1,0,1]): {list(itertools.compress('ABCDE', [1,0,1,0,1,1,0]))}")

# islice(interable, start, stop, step)
print(f"islice(range(10), 2, 8, 2): {list(itertools.islice(range(10), 2, 8, 2))}")

# groupby()
data = [("A", 1), ("A", 2), ("B", 3), ("B", 4), ("A", 5)]
data.sort() # groupby works on pre-sorted data
grouped = { k : list(v) for k, v in itertools.groupby(data, lambda x: x[0])}
print(f"groupby results: {grouped}")
