from datetime import datetime
import math
import datetime
import random
import os
import sys

# 1. math module
print("--- math module ---")
print(f"Value of pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"Factorial of 5: {math.factorial(5)}")

# 2. datetime module
print("\n--- datetime module ---")
now = datetime.datetime.now()
month = datetime.datetime.now().month
print(month)
print(f"Current Date and Time: {now}")
print(f"Current Year: {now.year}")
print(f"Formatted Date: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# 3. random module
print("\n--- random module ---")
print(f"Random float between 0 and 1: {random.random()}")
print(f"Random integer between 1 and 100: {random.randint(1, 100)}")
colors = ['red', 'green', 'blue']
print(f"Random choice from list: {random.choice(colors)}")


# 4. os module
print("\n--- os module ---")
print(f"Current Working Directory: {os.getcwd()}")
print(f"Operating System: {os.name}")
print(os.cpu_count())
print(os.device_encoding(fd=sys.stdout.fileno()))
print(os.environ.get('USER'))

# 5. sys module
print("\n--- sys module ---")
print(f"Python Version: {sys.version}")
print(f"Platform: {sys.platform}")
