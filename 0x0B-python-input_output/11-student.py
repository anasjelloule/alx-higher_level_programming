#!/usr/bin/python3
# Anas Jelloul
"""Impliment class Student."""


class Student:
    """Class student."""

    def __init__(self, first_name, last_name, age):
        """Init a new Student.

        Args:
            first_name (str): first
            last_name (str): last name
            age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of the Student."""
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace every attribute of the Student.

        Args:
            json (dict): key/value pairs to replace with.
        """
        for k, v in json.items():
            setattr(self, k, v)
