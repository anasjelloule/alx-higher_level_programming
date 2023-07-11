#!/usr/bin/python3
# ANAS Jelloul
"""append to fil creates i not"""


def append_write(filename="", text=""):
    """append to file or creates i not
    Args:
        filename (str): name of the file to append.
        text (str): string to append in the file.
    Returns:
       number of characters.
    """
    
    with open(filename, mode="a+", encoding='utf-8') as f:
        return(f.write(text))
