#!/usr/bin/python3
"""
A class Square that defines a square
"""


class Square:
    """
    First time with setter
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    def area(self):
        return (self._Square__size * self._Square__size)
