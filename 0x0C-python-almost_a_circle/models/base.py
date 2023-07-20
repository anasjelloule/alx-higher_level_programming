#!/usr/bin/python3
# Anas Jelloul
"""Impliment a base model class."""
import json
import csv


class Base:
    """Class base model.

    Represents the "base" for all Inheritence classes in project 0x0C*.

    Attributes:
        __nb_objects (int): Number.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Init a Base.

        Args:
            id (int): Identity Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON "serialized list dicts".

        Args:
            list_dictionaries (list): A dictionaries list.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON "serialized list dicts".

        Args:
            list_objs (list): A dictionaries list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialized of JSON string.

        Args:
            json_string (str): A JSON str list of dicts.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return  instantied class from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialized.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                nw = cls(1, 1)
            else:
                nw = cls(1)
            nw.update(**dictionary)
            return nw

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
