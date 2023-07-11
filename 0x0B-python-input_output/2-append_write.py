#!/usr/bin/python3
"""append to fil creates i not"""


def append_write(filename="", text=""):
    """append to file or creates i not"""
    with open(filename, mode="a+", encoding='utf-8') as f:
        return(f.write(text))
