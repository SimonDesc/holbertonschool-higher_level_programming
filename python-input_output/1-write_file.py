#!/usr/bin/python3
""" function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """open and write"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            nb_characters = f.write(text)
    except IOError:
        pass
    return nb_characters
