#!/usr/bin/python3
"""first class"""
import json


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
