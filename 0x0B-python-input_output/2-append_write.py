#!/usr/bin/python3
# Anas Jelloul
"""Impliment file-appending function."""


def append_write(filename="", text=""):
    """Insert a string to the end of a UTF8 text file.

    Args:
        filename (str): name_file.
        text (str): string insert.
    Returns:
        Number characters Inserted.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
