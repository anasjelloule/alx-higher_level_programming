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
        """return area"""
        return self.height * self.width

    def perimeter(self):
        """ return perimeter
        """
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        """return  printable rect """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rct = []
        for i in range(self.__height):
            [rct.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rct.append("\n")
        return ("".join(rct))

    def __repr__(self):
        """return modifie repr """
        rct = "Rectangle(" + str(self.__width)
        rct += ", " + str(self.__height) + ")"
        return (rct)
