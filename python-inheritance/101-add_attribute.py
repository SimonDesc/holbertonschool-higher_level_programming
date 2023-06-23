#!/usr/bin/python3
"""function that block the creation of new attr"""


def add_attribute(object, type, string):
    """check if the attr is in dict or slots"""
    if not hasattr(object, '__dict__') or (hasattr(object, '__slots__') and type not in object.__slots__):
        raise TypeError("can't add new attribute")
    setattr(object, type, string)
