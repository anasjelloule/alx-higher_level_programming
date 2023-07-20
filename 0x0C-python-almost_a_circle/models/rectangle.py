#!/usr/bin/python3
# Anas Jelloul
"""Impliment an inheritence rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent an inheritence rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Init a new Rectangle.

        Args:
            width (int): width.
            height (int): height.
            x (int): x coordinate.
            y (int): y coordinate.
            id (int): identity.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
