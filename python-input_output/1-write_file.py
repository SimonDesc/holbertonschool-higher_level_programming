#!/usr/bin/python3
""" function that writes a string to a text file (UTF8) and 
returns the number of characters written"""


def write_file(filename="", text=""):
    """open and write"""
    try:
        with open(filename, "w", encoding="utf-8") as f:
            nb_characters = f.write(text)
            return nb_characters
    except IOError:
        pass
