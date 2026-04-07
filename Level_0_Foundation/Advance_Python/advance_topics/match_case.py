"""
Structural Pattern Matching (match-case) - Python 3.10+
======================================================

Structural pattern matching is a powerful feature introduced in Python 3.10. 
It allows you to match complex data structures against patterns, making code 
more readable and expressive than traditional if-elif-else chains.

Key Syntax:
match subject:
    case <pattern_1>:
        <action_1>
    case <pattern_2> if <condition>:
        <action_2>
    case _:
        <default_action>
"""

import sys

def check_python_version():
    """Ensure we are running on Python 3.10 or higher.""" # example of docstring
    if sys.version_info < (3, 10):
        print("❌ Error: match-case requires Python 3.10 or higher.")
        print(f"Current version: {sys.version}")
        return False
    return True

# --------------------------------------------------------------------------
# 1. Basic Literal Matching
# --------------------------------------------------------------------------
def basic_match(status_code):
    print(f"\n[1] Basic Match: Handling Status Code {status_code}")
    match status_code:
        case 200:
            print("OK")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
        case _:
            print("Unknown Status Code")

# --------------------------------------------------------------------------
# 2. Or Pattern (|)
# --------------------------------------------------------------------------
def or_pattern_match(day):
    print(f"\n[2] OR Pattern: Handling Day '{day}'")
    match day.lower():
        case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
            print("It's a weekday. Time to work!")
        case "saturday" | "sunday":
            print("It's the weekend! Time to relax.")
        case _:
            print("Not a valid day.")

# --------------------------------------------------------------------------
# 3. Sequence Patterns (Lists/Tuples)
# --------------------------------------------------------------------------
def sequence_match(command):
    print(f"\n[3] Sequence Match: Command {command}")
    match command:
        case ["quit"]:
            print("Exiting...")
        case ["load", filename]:
            print(f"Loading file: {filename}")
        case ["save", filename, "--force"]:
            print(f"Force saving file: {filename}")
        case ["save", filename]:
            print(f"Saving file: {filename}")
        case ["move", x, y]:
            print(f"Moving to coordinates ({x}, {y})")
        case ["move", *coords]: # Capturing multiple elements
            print(f"Moving through points: {coords}")
        case _:
            print("Invalid command.")

# --------------------------------------------------------------------------
# 4. Mapping Patterns (Dictionaries)
# --------------------------------------------------------------------------
def mapping_match(user_data):
    print(f"\n[4] Mapping Match: User Data {user_data}")
    match user_data:
        case {"name": name, "role": "admin"}:
            print(f"Logged in as ADMIN: {name}")
        case {"name": name, "role": role}:
            print(f"Logged in as {role}: {name}")
        case {"id": user_id}:
            print(f"Anonymous User ID: {user_id}")
        case _:
            print("Guest user.")

# --------------------------------------------------------------------------
# 5. Class Patterns (Objects)
# --------------------------------------------------------------------------
class Point:
    __match_args__ = ("x", "y") # Helper for positional matching
    def __init__(self, x, y):
        self.x = x
        self.y = y

def class_match(point):
    print(f"\n[5] Class Match: Point({point.x}, {point.y})")
    match point:
        case Point(x=0, y=0):
            print("Origin point.")
        case Point(x=0, y=y):
            print(f"On the Y-axis at {y}.")
        case Point(x=x, y=0):
            print(f"On the X-axis at {x}.")
        case Point(x, y): # Requires __match_args__
            print(f"Point at ({x}, {y}).")
        case _:
            print("Not a point.")

# --------------------------------------------------------------------------
# 6. Guards (Adding 'if' conditions)
# --------------------------------------------------------------------------
def guard_match(point):
    print(f"\n[6] Guards: Conditional logic for Point({point.x}, {point.y})")
    match point:
        case Point(x, y) if x == y:
            print(f"Point is on the Y=X line: ({x}, {y})")
        case Point(x, y) if x == -y:
            print(f"Point is on the Y=-X line: ({x}, {y})")
        case Point(x, y):
            print(f"Any other point: ({x}, {y})")

# --------------------------------------------------------------------------
# 7. AS Patterns (Capturing the whole thing)
# --------------------------------------------------------------------------
def as_pattern_match(data):
    print(f"\n[7] AS Patterns: Capturing whole object from {data}")
    match data:
        case [Point(x, y) as p1, Point(x2, y2) as p2]:
             print(f"Segment between {p1} and {p2}")
             print(f"Coordinates: ({x}, {y}) to ({x2}, {y2})")
        case _:
            print("No segment found.")

# --------------------------------------------------------------------------
# RUNNING THE EXAMPLES
# --------------------------------------------------------------------------
if __name__ == "__main__":
    if check_python_version():
        # Literal matches
        basic_match(200)
        basic_match(404)
        basic_match(505)

        # Or patterns
        or_pattern_match("Monday")
        or_pattern_match("Sunday")

        # Sequence matches
        sequence_match(["load", "data.csv"])
        sequence_match(["save", "backup.zip", "--force"])
        sequence_match(["move", 10, 20])
        sequence_match(["move", 1, 2, 3, 4, 5])

        # Mapping matches
        mapping_match({"name": "Alice", "role": "admin"})
        mapping_match({"name": "Bob", "role": "user"})
        mapping_match({"id": 12345})

        # Class matches
        class_match(Point(0, 0))
        class_match(Point(0, 5))
        class_match(Point(10, 20))

        # Guards
        guard_match(Point(5, 5))
        guard_match(Point(5, -5))
        guard_match(Point(1, 2))

        # AS patterns
        as_pattern_match([Point(0,0), Point(1,1)])

        print("\n✅ All demonstrations complete.")
