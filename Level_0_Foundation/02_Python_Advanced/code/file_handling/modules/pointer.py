"""
Pointer Module
==============
Handles seek, tell, and flush operations.
"""

def get_pointer_position(filename):
    """Returns the current position of the pointer in a file."""
    file = open(filename, "r")
    pos = file.tell()
    file.close()
    return pos

def read_from_offset(filename, offset):
    """Seeks to an offset and reads from there."""
    file = open(filename, "r")
    file.seek(offset)
    content = file.read()
    file.close()
    return content

def flush_write(filename, content):
    """Writes content and flushes the buffer."""
    file = open(filename, "w")
    file.write(content)
    file.flush()
    file.close()
    return True
