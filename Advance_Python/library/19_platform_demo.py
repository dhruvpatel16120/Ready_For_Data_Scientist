import platform

"""
Python platform Module
Provides an API for retrieving information about the underlying platform (operating system, hardware, and python interpreter).
"""

print(f"Platform: {platform.platform()}")
print(f"System: {platform.system()}")
print(f"Node: {platform.node()}")
print(f"Release: {platform.release()}")
print(f"Version: {platform.version()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}")

print("\n--- Architecture and Python info ---")
print(f"Architecture: {platform.architecture()}")
print(f"Python Build: {platform.python_build()}")
print(f"Python Compiler: {platform.python_compiler()}")
print(f"Python Implementation: {platform.python_implementation()}")
print(f"Python Version: {platform.python_version()}")

# Detailed OS info (on Windows/Mac/Linux)
# print(f"uname: {platform.uname()}")
