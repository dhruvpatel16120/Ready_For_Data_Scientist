"""
Writing Module
==============
Handles different writing operations for file handling.
"""

def write_to_file(filename, content):
    """Writes a string to a file, overwriting existing content."""
    file = open(filename, "w")
    file.write(content)
    file.close()
    return True

def write_multiple_lines(filename, lines_list):
    """Writes a list of strings to a file."""
    file = open(filename, "w")
    file.writelines(lines_list)
    file.close()
    return True

def append_to_file(filename, content):
    """Appends content to the end of a file."""
    file = open(filename, "a")
    file.write(content)
    file.close()
    return True
