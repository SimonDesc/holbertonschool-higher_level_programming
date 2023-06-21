#!/usr/bin/python3
"""reads a text file and prints it to stdout"""


def read_file(filename=""):
    """open and read a file"""
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
