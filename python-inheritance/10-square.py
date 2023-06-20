#!/usr/bin/python3
""" Class Rectangle that inherits from BaseGeometry"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """Returns a string that can be used to recreate the rectangle"""
        return f"[Rectangle] {self.__size}/{self.__size}"

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__size * 2
