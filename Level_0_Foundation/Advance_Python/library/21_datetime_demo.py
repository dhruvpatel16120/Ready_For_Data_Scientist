from datetime import datetime, date, time, timedelta

"""
Python datetime Module
Supplies classes for manipulating dates and times.
"""

# 1. Current datetime
now = datetime.now()
print(f"Now: {now}")
print(f"Today: {date.today()}")

# 2. Creating specific dates/times
d = date(2025, 12, 25)
t = time(10, 30, 45)
dt = datetime(2025, 12, 25, 10, 30, 45)
print(f"Custom Date: {d}")
print(f"Custom DateTime: {dt}")

# 3. Formatting and Parsing (strptime / strftime)
dt_str = "2024-01-01 12:00:00"
parsed_dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
print(f"Parsed: {parsed_dt}")
print(f"Formatted: {parsed_dt.strftime('%A, %d %B %Y')}")

# 4. Timedelta (Arithmetic with dates)
tomorrow = now + timedelta(days=1)
last_week = now - timedelta(weeks=1)
print(f"Tomorrow: {tomorrow}")
print(f"Last Week: {last_week}")

diff = tomorrow - now
print(f"Difference: {diff.total_seconds()} seconds")

# 5. Extracting components
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")
print(f"Weekday (0-6): {now.weekday()}") # 0 is Monday
