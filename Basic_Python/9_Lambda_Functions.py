# Lambda Functions in Python

# A lambda function is a small anonymous function defined with the lambda keyword.
# It can take any number of arguments but can only have one expression.
# lambda arguments: expression , where arguments are like parameters and expression is like function body
even = lambda x: x % 2 == 0
square = lambda x: x * x
add = lambda a, b: a + b

print("Is 4 even?", even(4))
print("Square of 5:", square(5))
print("Addition of 3 and 7:", add(3, 7))

# lambda function with map
numbers = [1, 2, 3, 4]
result = list(map(lambda x: x * 2, numbers))
print(result)

# lambda function with filter
data = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0, data))
print(result)

# lambda function with sorted
data = [(1, 3), (4, 1), (2, 2)]
result = sorted(data, key=lambda x: x[0])

print(result)

