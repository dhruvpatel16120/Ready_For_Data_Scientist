"""
Reading Module
==============
Handles different reading operations for file handling.
"""

def read_entire_file(filename):
    """Reads the entire content of a file."""
    try:
        file = open(filename, "r")
        content = file.read()
        file.close()
        return content
    except FileNotFoundError:
        return "Error: File not found."

def read_by_characters(filename, num_chars):
    """Reads a specific number of characters from a file."""
    try:
        file = open(filename, "r")
        content = file.read(num_chars)
        file.close()
        return content
    except FileNotFoundError:
        return "Error: File not found."

def read_single_line(filename):
    """Reads a single line from a file."""
    try:
        file = open(filename, "r")
        line = file.readline()
        file.close()
        return line
    except FileNotFoundError:
        return "Error: File not found."

def read_all_lines(filename):
    """Reads all lines and returns them as a list."""
    try:
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        return lines
    except FileNotFoundError:
        return []
