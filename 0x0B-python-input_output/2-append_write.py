#!/usr/bin/python3
# ANAS Jelloul
"""append to fil creates i not"""


def append_write(filename="", text=""):
    """Return number of characters."""
    with open(filename, mode="a+", encoding='utf-8') as f:
        return(f.write(text))
