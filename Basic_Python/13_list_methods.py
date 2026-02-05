# List Methods Demonstration Program

numbers = [10, 20, 30]
print("Initial List:", numbers)

# append() – add element at the end
numbers.append(40)
print("After append(40):", numbers)

# extend() – add multiple elements
numbers.extend([50, 60])
print("After extend([50, 60]):", numbers)

# insert() – insert at specific index
numbers.insert(2, 25)
print("After insert(2, 25):", numbers)

# remove() – remove first occurrence of value
numbers.remove(25)
print("After remove(25):", numbers)

# pop() – remove by index (last element if no index)
removed = numbers.pop()
print("After pop():", numbers)
print("Popped element:", removed)

removed = numbers.pop(1)
print("After pop(1):", numbers)
print("Popped element:", removed)

# count() – count occurrences
numbers.append(20)
print("After append(20):", numbers)
print("Count of 20:", numbers.count(20))

# index() – find index of element
print("Index of 20:", numbers.index(20))

# sort() – sort list in ascending order
numbers.sort()
print("After sort():", numbers)

# reverse() – reverse list
numbers.reverse()
print("After reverse():", numbers)

# copy() – create a shallow copy
copy_list = numbers.copy()
print("Copied list:", copy_list)

# clear() – remove all elements
numbers.clear()
print("After clear():", numbers)
