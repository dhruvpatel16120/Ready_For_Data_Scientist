# Type Casting in Python

# Implicit Type Casting
x = 5           # Integer
y = 2.0         # Float
z = x + y      # Implicitly converts x to float and adds

print("Implicit Type Casting:")
print("x (int):", x)
print("y (float):", y)
print("z (x + y):", z)
print("Type of z:", type(z))
print()

# Explicit Type Casting
a="10"        # String
b=5           # Integer
c=float(b)    # Explicitly converts b to float
d=int(a)      # Explicitly converts a to integer
e=str(b)      # Explicitly converts b to string
f=bool(b)     # Explicitly converts b to boolean

print("Explicit Type Casting:")
print("a (string):", a)
print("b (int):", b)
print("c (float of b):", c)
print("d (int of a):", d)
print("e (string of b):", e)
print("f (boolean of b):", f)
print("Type of c:", type(c))
print("Type of d:", type(d))
print("Type of e:", type(e))
print("Type of f:", type(f))
print()
