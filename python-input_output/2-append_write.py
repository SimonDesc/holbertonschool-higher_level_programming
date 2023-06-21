#!/usr/bin/python3
"""function appends a string at the end of a text file (UTF8"""


def append_write(filename="", text=""):
    """append"""
    with open(filename, "a", encoding="utf-8") as f:
        nb_characters = f.write(text)
    return nb_characters
