def greet(name):
    """A simple function to greet a user."""
    return f"Hello, {name}! Welcome to the world of Python modules."

def add_numbers(a, b):
    """A function that returns the sum of two numbers."""
    return a + b

PI_VALUE = 3.14159
# print(__name__)
# print(greet("John"))

if __name__ == "__main__":
    print(greet("John"))
    print(add_numbers(10, 20))
    print(PI_VALUE)
