#!/usr/bin/python3
"""defines class of rectangle."""


class Rectangle:
    """ rectangle."""
    def __init__(self, width=0, height=0):
        """init rectangle.

        Args:
            width (int): The width .
            height (int): The height.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area"""
        return self.height * self.width

    def perimeter(self):
        """ returns perimeter
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)
