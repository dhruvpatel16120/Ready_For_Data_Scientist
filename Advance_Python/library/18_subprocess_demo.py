import subprocess

"""
Python subprocess Module
Allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
"""

# 1. Running a simple command (Portable way to check ping or list files)
print("--- Running 'echo' command ---")
try:
    # On Windows: 'echo', on Unix 'echo'
    # Use shell=True with caution
    result = subprocess.run(["echo", "Hello from Subprocess"], capture_output=True, text=True, shell=True)
    print(f"Stdout: {result.stdout}")
    print(f"Return Code: {result.returncode}")
except Exception as e:
    print(f"Error: {e}")

# 2. capturing output of 'dir' on Windows or 'ls' on Unix
print("\n--- Listing directory ---")
cmd = "dir" # Windows specific
result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
print(f"First 100 characters of output:\n{result.stdout[:100]}...")

# 3. Handling errors
print("\n--- Handling Errors ---")
try:
    subprocess.run(["non_existent_command"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed: {e}")
except FileNotFoundError:
    print("Command not found!")

# 4. Check outputs with check_output
# output = subprocess.check_output(["echo", "Test output"], shell=True)
# print(output.decode())
