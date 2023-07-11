#!/usr/bin/python3
# Anas Jelloul
"""Impliment insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.

    Args:
        filename (str): name_file.
        search_string (str): searched string.
        new_string (str): string to be inserted.
    """
    txt = ""
    with open(filename) as r:
        for ln in r:
            txt += ln
            if search_string in ln:
                txt += new_string
    with open(filename, "w") as w:
        w.write(txt)
