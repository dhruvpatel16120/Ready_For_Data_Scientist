import heapq

"""
Python heapq Module
Provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.
Min-heap by default.
"""

data = [5, 2, 8, 1, 9, 3]
print(f"Original data: {data}")

# Convert list to heap in-place
heapq.heapify(data)
print(f"Heapified: {data}")

# Push and Pop
heapq.heappush(data, 4)
print(f"After pushing 4: {data}")

smallest = heapq.heappop(data)
print(f"Popped smallest: {smallest}")
print(f"Current heap: {data}")

# Push and then Pop (heappushpop)
result = heapq.heappushpop(data, 0)
print(f"Pushed 0 and popped (heappushpop): {result}")

# Replace (pop then push)
result = heapq.heapreplace(data, 10)
print(f"Popped smallest and pushed 10 (heapreplace): {result}")
print(f"Queue after replace: {data}")

print("\n--- n largest/smallest elements ---")
nums = [1, 5, 3, 2, 8, 5, 0]
print(f"3 Largest: {heapq.nlargest(3, nums)}")
print(f"3 Smallest: {heapq.nsmallest(3, nums)}")

# Priority Queue Example with Tuples
pq = []
heapq.heappush(pq, (3, "Task 3"))
heapq.heappush(pq, (1, "Task 1"))
heapq.heappush(pq, (2, "Task 2"))

print("\nPriority Queue Consumption:")
while pq:
    priority, task = heapq.heappop(pq)
    print(f"Processing {task} with priority {priority}")
