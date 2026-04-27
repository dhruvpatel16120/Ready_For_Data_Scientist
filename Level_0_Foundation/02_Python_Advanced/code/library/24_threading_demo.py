import threading
import time

"""
Python threading Module
Higher-level threading interface.
"""

def task(name, delay):
    print(f"Thread {name} starting...")
    time.sleep(delay)
    print(f"Thread {name} finished after {delay} seconds.")

# 1. Creating and starting threads
print("--- Threading Demo ---")
t1 = threading.Thread(target=task, args=("A", 2))
t2 = threading.Thread(target=task, args=("B", 1))

t1.start()
t2.start()

# 2. join() - Wait for thread to finish
print("Waiting for threads to complete...")
t1.join()
t2.join()
print("Main thread continues.")

# 3. Thread safety (Lock)
counter = 0
lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock: # Protect shared resource
            counter += 1

threads = []
for i in range(5):
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"\nFinal Counter Value: {counter}")
