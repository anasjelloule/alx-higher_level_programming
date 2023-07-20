#!/usr/bin/python3
# Anas Jelloul
"""Impliment Impliment an inheritence square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent an inheritence square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Init a new Square.

        Args:
            size (int): size.
            x (int): x coordinate.
            y (int): y coordinate.
            id (int): identity.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): Set attribute values.
                - 1st argument_represents id attribute
                - 2nd argument_represents size attribute
                - 3rd argument_represents x attribute
                - 4th argument_represents y attribute
            **kwargs (dict): New key/value pairs.
        """
        if args and len(args) != 0:
            ch = 0
            for arg_ in args:
                if ch == 0:
                    if arg_ is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg_
                elif ch == 1:
                    self.size = arg_
                elif ch == 2:
                    self.x = arg_
                elif ch == 3:
                    self.y = arg_
                ch += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of current Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of current Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
