import asyncio
import time

"""
Python asyncio Module
Library to write concurrent code using the async/await syntax.
Best for I/O-bound tasks.
"""

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"Started at {time.strftime('%X')}")

    # 1. Running tasks concurrently
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    # Wait for both tasks to finish
    await task1
    await task2

    print(f"Finished at {time.strftime('%X')}")

    # 2. asyncio.gather - cleaner way for multiple tasks
    print("\n--- asyncio.gather ---")
    results = await asyncio.gather(
        say_after(0.5, "Quick task"),
        say_after(1.5, "Slow task")
    )

# Run the event loop
if __name__ == "__main__":
    asyncio.run(main())
