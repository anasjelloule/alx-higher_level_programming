#!/usr/bin/python3
# Anas Jelloul
"""Impliment class Rectangle inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Init new Rectangle.

        Args:
            width (int): Width.
            height (int): Height.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
