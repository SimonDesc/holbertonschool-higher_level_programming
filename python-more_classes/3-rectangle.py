#!/usr/bin/python3
""" Print a rectangle """


class Rectangle:
    """
    Return dimension of a Rectangle
    """

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    def __str__(self):
        str = ""
        for i in range(self.height):
            for j in range(self.width):
                str += "#"
            if i != self.height - 1:
                str += "\n"
        return str

    @property
    def width(self):
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self._Rectangle__width = value

    @property
    def height(self):
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self._Rectangle__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.height + self.width) * 2
