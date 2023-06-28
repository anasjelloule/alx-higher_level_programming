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
            size (int): size of square Default 0.

        Raises:
            TypeError: size must integer
            ValueError: size must >= 0
        """
        self.__size = size
        if type(self.__size) != int:
            raise TypeError('size must be an integer')
        elif self.__size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """ finding the area of the square

        Returns:
            int: the are of the square
        """
        return self.__size**2
