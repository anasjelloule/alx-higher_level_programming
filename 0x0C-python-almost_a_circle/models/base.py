#!/usr/bin/python3
# Anas Jelloul
"""Impliment a base model class."""


class Base:
    """Class base model.

    Represents the "base" for all Inheritence classes in project 0x0C*.

    Attributes:
        __nb_objects (int): Number.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Init a new Base.

        Args:
            id (int): Identity new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
