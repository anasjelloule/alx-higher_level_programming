#!/usr/bin/python3
"""Fn read File."""


def read_file(filename=""):
    """core Fn read File."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
