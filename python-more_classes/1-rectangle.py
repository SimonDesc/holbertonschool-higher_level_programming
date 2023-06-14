#!/usr/bin/python3
""" Print a rectangle """


class Rectangle:
    """
    Return dimension of a Rectangle
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self._Rectangle_width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._Rectangle_width = value

    @property
    def height(self):
        return self._Rectangle_height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._Rectangle_height = value
