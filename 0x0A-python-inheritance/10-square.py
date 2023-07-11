#!/usr/bin/python3
# Anas Jelloul
"""Impliment Rectangle Square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent square."""

    def __init__(self, size):
        """Init a new square.

        Args:
            size (int): Size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
