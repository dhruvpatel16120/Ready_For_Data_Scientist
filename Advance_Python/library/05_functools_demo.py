import functools
import time

"""
Python functools Module
Higher-order functions and operations on callable objects.
"""

# 1. lru_cache (Last Recently Used Cache)
@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

start = time.time()
print(f"Fibonacci(35): {fibonacci(35)}")
print(f"Time taken with cache: {time.time() - start:.5f}s")
print(f"Cache Info: {fibonacci.cache_info()}")

# 2. partial
def power(base, exponent):
    return base ** exponent

square = functools.partial(power, exponent=2)
cube = functools.partial(power, exponent=3)

print(f"\nSquare of 5: {square(5)}")
print(f"Cube of 5: {cube(5)}")

# 3. reduce
nums = [1, 2, 3, 4, 5]
product = functools.reduce(lambda x, y: x * y, nums)
print(f"\nProduct of {nums}: {product}")

# 4. wraps (decorator boilerplate)
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        print("Before call")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Example docstring"""
    print("Inside example")

print(f"\nFunction name: {example.__name__}")
print(f"Function doc: {example.__doc__}")

# 5. singledispatch (Generic functions)
@functools.singledispatch
def process(arg):
    print(f"Base implementation: {arg}")

@process.register(int)
def _(arg):
    print(f"Processing integer: {arg}")

@process.register(list)
def _(arg):
    print(f"Processing list of length: {len(arg)}")

print("\n--- singledispatch ---")
process("Hello")
process(100)
process([1, 2, 3])
