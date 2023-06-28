#!/usr/bin/python3
"""class Square."""


class Square():
    """ class calculate square
    Args:
        square (class): define class . square size
    """

    def __init__(self, size=0):
        """init square

        Args:
            size (int): the size of the square passed. Defaults to 0.

        Raises:
            TypeError: size must integer
            ValueError: size must>= 0
        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')

    @property
    def size(self):
        """getter for size

        Returns:
            integer:val of private size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setterr

        Args:
            value (int): size value

        Raises:
            TypeError: ifnot integer
            ValueError: if< 0
        """

        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')

        self.__size = value

    def area(self):
        """ finding area of square

        Returns:
            int:areq of square
        """
        return self.__size**2
