import random

"""
Python random Module
Implements pseudo-random number generators for various distributions.
"""

print("--- Random Numbers ---")
print(f"random(): {random.random()}") # float in [0.0, 1.0)
print(f"uniform(1, 10): {random.uniform(1, 10)}") # float in [1, 10]
print(f"randint(1, 10): {random.randint(1, 10)}") # int in [1, 10] inclusive
print(f"randrange(0, 100, 5): {random.randrange(0, 100, 5)}") # int from range

print("\n--- Working with Sequences ---")
items = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry']
print(f"Original items: {items}") 
print(f"choice(items): {random.choice(items)}")
print(f"choices(items, k=2): {random.choices(items, k=2)}") # with replacement
print(f"sample(items, k=2): {random.sample(items, k=2)}") # without replacement

random.shuffle(items)
print(f"After shuffle(items): {items}")

print("\n--- Distributions ---")
print(f"gauss(mu=0, sigma=1): {random.gauss(0, 1)}")
print(f"expovariate(lambd=1.0): {random.expovariate(1.0)}")

# Seeding for reproducibility
random.seed(42)
print(f"Random with seed 42: {random.random()}")
random.seed(42)
print(f"Random with seed 42 again: {random.random()}")
