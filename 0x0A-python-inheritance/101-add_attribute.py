#!/usr/bin/python3
# Anas Jelloul
"""Impliment function adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to object if it possible.

    Args:
        obj (any): Obj.
        att (str): Name.
        value (any): value att.
    Raises:
        TypeError: If cannot add attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
