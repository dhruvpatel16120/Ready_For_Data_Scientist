# Lambda Functions in Python

# A lambda function is a small anonymous function defined with the lambda keyword.
# It can take any number of arguments but can only have one expression.

even = lambda x: x % 2 == 0
square = lambda x: x * x
add = lambda a, b: a + b

print("Is 4 even?", even(4))
print("Square of 5:", square(5))
print("Addition of 3 and 7:", add(3, 7))

# recursion in python
# recursion is the process in which a function calls itself directly or indirectly.
print("recursion in python")

# solve factorial using recursion
def factorial(n):
    # base case 
    if n == 0 or n == 1:
        return 1
    # recursive case
    else:
        return n * factorial(n - 1)