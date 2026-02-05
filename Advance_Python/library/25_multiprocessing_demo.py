import multiprocessing
import time
import os

"""
Python multiprocessing Module
Supports spawning processes using an API similar to the threading module.
Bypasses the Global Interpreter Lock (GIL).
"""

def square(n):
    print(f"Process {os.getpid()} calculating square of {n}")
    time.sleep(0.5)
    return n * n

if __name__ == "__main__":
    # Note: On Windows, multiprocessing code MUST be under 'if __name__ == "__main__":'
    
    # 1. Using Process class directly
    p = multiprocessing.Process(target=square, args=(10,))
    p.start()
    p.join()

    # 2. Using a Pool (Parallel processing)
    print("\n--- Multiprocessing Pool ---")
    numbers = [1, 2, 3, 4, 5]
    
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(square, numbers)
    
    print(f"Results: {results}")

    # 3. Shared state (using Value or Array)
    # multiprocessing.Value('i', 0)
