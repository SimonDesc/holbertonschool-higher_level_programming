#!/usr/bin/python3
"""
A class Square that defines a square
"""


class Square:
    """
    A class that check the size
    and return the area
    """

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = size

    def area(self):
        return (self._Square__size * self._Square__size)
