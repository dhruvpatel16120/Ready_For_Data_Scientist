import sqlite3
import math

def custom_functions_demo():
    print("--- SQLite: Custom Python Functions & In-Memory DB ---")
    
    # 1. Create an In-Memory Database
    # Using ':memory:' creates a database that exists only in RAM.
    # It is extremely fast and perfect for unit tests.
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # 2. Define a Python function to use in SQL
    def calculate_circle_area(radius):
        """A Python function we want to call from SQL."""
        return math.pi * (radius ** 2)

    # 3. Register the function with SQLite
    # Parameters: name in SQL, number of args, the Python function
    conn.create_function("circle_area", 1, calculate_circle_area)

    # 4. Use the custom function in a query
    print("Calculating circle areas using a custom SQL function:")
    cursor.execute("CREATE TABLE circles (name TEXT, radius REAL)")
    cursor.executemany("INSERT INTO circles VALUES (?, ?)", [("Small", 2.0), ("Medium", 5.0), ("Large", 10.0)])

    cursor.execute("SELECT name, radius, circle_area(radius) FROM circles")
    for name, radius, area in cursor.fetchall():
        print(f"{name} Circle (r={radius}): Area = {area:.2f}")

    # 5. Define a custom Aggregate function
    class ProductAggregate:
        def __init__(self):
            self.product = 1
        def step(self, value):
            self.product *= value
        def finalize(self):
            return self.product

    conn.create_aggregate("product", 1, ProductAggregate)
    
    cursor.execute("SELECT product(radius) FROM circles")
    total_product = cursor.fetchone()[0]
    print(f"\nProduct of all radii: {total_product}")

    conn.close()
    print("\nCustom functions demo completed (In-Memory DB vanished).\n")

if __name__ == "__main__":
    custom_functions_demo()
