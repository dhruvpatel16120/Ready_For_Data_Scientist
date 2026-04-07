from collections import namedtuple, deque, Counter, OrderedDict, defaultdict

"""
Python collections Module
Specialized container datatypes providing alternatives to Python’s general purpose built-in containers.
"""

# 1. namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"NamedTuple: Point(x={p.x}, y={p.y})")

# 2. deque (Double Ended Queue)
d = deque(['a', 'b', 'c'])
d.append('d')
d.appendleft('x')
print(f"\nDeque: {d}")
d.pop()
d.popleft()
print(f"Deque after pops: {d}")

# 3. Counter
text = "gallahad"
c = Counter(text)
print(f"\nCounter for '{text}': {c}")
print(f"Most common 2: {c.most_common(2)}")

# 4. defaultdict
dd = defaultdict(int) # default value 0
dd['a'] += 1
print(f"\nDefaultDict (int): {dd['a']}, {dd['b']}")

dd_list = defaultdict(list)
dd_list['fruits'].append('apple')
print(f"DefaultDict (list): {dd_list}")

# 5. OrderedDict (Preserves insertion order - default in Python 3.7+ dict)
od = OrderedDict()
od['a'] = 1
od['b'] = 2
print(f"\nOrderedDict: {od}")

# 6. ChainMap (not demoed here but worth knowing - groups multiple dicts)
from collections import ChainMap
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
chain = ChainMap(dict1, dict2)
print(f"\nChainMap: {chain['b']} (from dict1), {chain['c']} (from dict2)")
