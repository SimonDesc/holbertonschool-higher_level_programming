#!/usr/bin/python3
""" Class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """width and height must be private. No getter or setter"""

    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        self.__width = width
        BaseGeometry.integer_validator(self, "height", height)
        self.__height = height

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__height * self.__width

    def __str__(self):
        """Returns a string that can be used to recreate the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
