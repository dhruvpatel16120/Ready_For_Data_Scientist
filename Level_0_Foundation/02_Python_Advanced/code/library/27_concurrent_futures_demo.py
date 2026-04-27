from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

"""
Python concurrent.futures Module
Provides a high-level interface for asynchronously executing callables.
"""

def task(n):
    print(f"Processing {n}")
    time.sleep(1)
    return f"Result of {n}"

def main():
    print("--- Using ThreadPoolExecutor ---")
    # Good for I/O bound tasks
    with ThreadPoolExecutor(max_workers=3) as executor:
        # map() returns results in order
        results = list(executor.map(task, [1, 2, 3]))
        print(f"Results: {results}")

    print("\n--- Using submit() for more control ---")
    with ThreadPoolExecutor(max_workers=3) as executor:
        future = executor.submit(task, 42)
        print(f"Future finished? {future.done()}")
        print(f"Future result: {future.result()}")

    # ProcessPoolExecutor is similar but uses processes (CPU bound)
    # with ProcessPoolExecutor() as executor:
    #     ...
    
if __name__ == "__main__":
    main()
