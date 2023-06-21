#!/usr/bin/python3
""" function that writes a string to a text file (UTF8)"""


def write_file(filename="", text=""):
    """open and write"""
    with open(filename, "w", encoding="utf-8") as f:
        nb_characters = f.write(text)
    return nb_characters
