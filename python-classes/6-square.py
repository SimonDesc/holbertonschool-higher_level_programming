#!/usr/bin/python3
"""
A class Square that defines a square
and print it , and now,
with more spaces !!
"""


class Square:
    """
    Printing a square
    with space
    """

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if type(position) != tuple or len(position) != 2 or \
           not all(isinstance(n, int) and n >= 0 for n in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._position = position

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

    def my_print(self):
        if self.size == 0:
            print()
        else:
            print('\n' * self.position[1], end='')
            for i in range(self.size):
                print(' ' * self.position[0], end='')
                print("#" * self.size)
