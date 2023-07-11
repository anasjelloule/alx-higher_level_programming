#!/usr/bin/python3
"""Wrte inside file"""


def write_file(filename="", text=""):
    """Edit a file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return(f.write(text))
