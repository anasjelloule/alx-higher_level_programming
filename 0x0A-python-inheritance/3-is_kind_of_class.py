#!/usr/bin/python3
# Anas Jelloul
"""Impliment class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if object an instance or inherited instance of class.

    Args:
        obj (any): instance.
        a_class (type): class match.
    Returns:
        If - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
