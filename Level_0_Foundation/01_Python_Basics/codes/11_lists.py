# list

# list creation
list_a = [1, 2, 3, 4, 5]
list_b = list("Hello")

# nested list
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# list operations
list_a[0] = 10 # Modify first element
concatenation = list_a + [6, 7, 8]
repetition = list_b * 3
slicing = list_a[1:4]
length = len(list_a)
reversed_list = list_a[::-1] # Slicing to reverse a list
reversed_list2 = list(reversed(list_a)) # Using reversed() function

# print results
print("Original list_a:", list_a)
print("Original list_b:", list_b)
print("Concatenation:", concatenation)
print("Repetition:", repetition)
print("Slicing:", slicing)
print("Length of list_a:", length)
print("Reversed list (slicing):", reversed_list)
print("Reversed list (function):",reversed_list2)