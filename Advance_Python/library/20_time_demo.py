import time

"""
Python time Module
Provides various time-related functions.
"""

# 1. Getting current time
seconds = time.time()
print(f"Seconds since epoch: {seconds}")

# 2. sleep (pauses execution)
print("Sleeping for 1 second...")
time.sleep(1)
print("Awake!")

# 3. time.ctime() - Converts seconds to a local time string
print(f"Local time: {time.ctime(seconds)}")

# 4. struct_time (Object representation)
local_struct = time.localtime()
print(f"Year: {local_struct.tm_year}")
print(f"Month: {local_struct.tm_mon}")
print(f"Day: {local_struct.tm_mday}")
print(f"Day of year: {local_struct.tm_yday}")
print(f"Hour: {local_struct.tm_hour}")
print(f"Minute: {local_struct.tm_min}")
print(f"Second: {local_struct.tm_sec}")
print(f"is DST: {local_struct.tm_isdst}")

# 5. formatting time
formatted = time.strftime("%Y-%m-%d %H:%M:%S", local_struct)
print(f"Formatted: {formatted}")

# 6. Performance profiling (monotonic time)
start = time.perf_counter()
# ... code to measure ...
time.sleep(0.5)
end = time.perf_counter()
print(f"Elapsed perf_counter time: {end - start:.5f}s")
