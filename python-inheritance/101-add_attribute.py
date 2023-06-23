#!/usr/bin/python3
"""function that block the creation of new attr"""


def add_attribute(obj, attr_name, attr_value):
    """
    The function adds a new attribute to an object if it is possible.

    Args
        obj (obj): The object to which the attribute needs to be added
        attr_name (str): The name of the attribute that we want to add
        attr_value (obj): The value of the attribute that we want to add

    Returns: nothing

    Raises:
        TypeError: if it's not possible to add a new attribute to the object
    """
    if not hasattr(obj, '__dict__') or (hasattr(obj, '__slots__')
                                        and attr_name not in obj.__slots__):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
