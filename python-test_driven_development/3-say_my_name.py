#!/usr/bin/python3
"""
Module that print the first and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Function print the name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))