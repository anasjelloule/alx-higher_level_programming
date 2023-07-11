#!/usr/bin/python3
# Anas Jelloul
"""Impliment inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): obj check.
        a_class (type): matched class.
    Returns:
        If - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
