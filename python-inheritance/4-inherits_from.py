#!/usr/bin/python3
"""A module with a class"""


def inherits_from(obj, a_class):
    """A class that return True or False"""

    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
