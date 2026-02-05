import math

"""
Python math Module
The math module provides access to the mathematical functions defined by the C standard.
"""

print("--- math basic constants ---")
print(f"PI: {math.pi}")
print(f"E: {math.e}")
print(f"Tau: {math.tau}")
print(f"Infinity: {math.inf}")
print(f"NaN: {math.nan}")

print("\n--- Power and Logarithmic Functions ---")
print(f"exp(3): {math.exp(3)}") # e^3
print(f"pow(2, 3): {math.pow(2, 3)}") # 2^3 (returns float)
print(f"log(10): {math.log(10)}") # natural log
print(f"log10(100): {math.log10(100)}") # base 10
print(f"sqrt(16): {math.sqrt(16)}")

print("\n--- Trigonometric Functions ---")
angle = math.radians(90) # convert to radians
print(f"sin(90deg): {math.sin(angle)}")
print(f"cos(90deg): {math.cos(angle)}")
print(f"tan(45deg): {math.tan(math.radians(45))}")

print("\n--- Rounding and Numeric ---")
print(f"ceil(4.2): {math.ceil(4.2)}") # rounds up
print(f"floor(4.8): {math.floor(4.8)}") # rounds down
print(f"fabs(-5.5): {math.fabs(-5.5)}") # absolute value
print(f"factorial(5): {math.factorial(5)}")
print(f"gcd(24, 36): {math.gcd(24, 36)}") # Greatest Common Divisor

# New in Python 3.8+
print(f"isqrt(15): {math.isqrt(15)}") # Integer square root (floor(sqrt(n)))
print(f"dist((0,0), (3,4)): {math.dist((0,0), (3,4))}") # Euclidean distance
