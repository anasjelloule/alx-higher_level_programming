#!/usr/bin/python3
# Anas Jelloul
"""Impliment class-checking function."""


def is_same_class(obj, a_class):
    """Check if the same instance of class.

    Args:
        obj (any): instance.
        a_class (type): class to compare with.
    Returns:
        If - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
