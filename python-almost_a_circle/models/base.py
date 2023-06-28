#!/usr/bin/python3
"""first class"""
import json
import os


class Base:
    """initialize an id"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []

        list_dictionaries = []
        for obj in list_objs:
            list_dictionaries.append(obj.to_dictionary())

        json_string = cls.to_json_string(list_dictionaries)

        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            **dictionary (dict): dict of set attributes
        """
        if cls.__name__ == "Rectangle":
            """width and height are mandatory attributes"""
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load JSON data from a file, convert it into python objects
        and return a list of these instances.

        Returns:
            list: a list of cls instances.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r") as f:
            obj = f.read()

        data_list = cls.from_json_string(obj)
        instances = []
        for data in data_list:
            instance = cls.create(**data)
            instances.append(instance)

        return instances
