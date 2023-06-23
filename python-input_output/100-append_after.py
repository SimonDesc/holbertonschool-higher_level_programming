#!/usr/bin/python3
"""search and add a new line in a txt file"""


def append_after(filename="", search_string="", new_string=""):
    """search and add"""
    with open(filename, "r+", encoding="utf-8") as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if search_string in line:
                lines.insert(i+1, new_string)
    with open(filename, 'w') as f:  # 'w' signifie "write"
        f.writelines(lines)
