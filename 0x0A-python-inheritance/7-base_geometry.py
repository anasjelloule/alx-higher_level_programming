#!/usr/bin/python3
# Anas Jelloul
"""Impliment base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """Not yet ."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate parameter as an integer.

        Args:
            name (str): name.
            value (int): value.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
