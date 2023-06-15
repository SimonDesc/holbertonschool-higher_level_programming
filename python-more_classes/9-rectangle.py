#!/usr/bin/python3
""" A module that defines a Rectangle class """

class Rectangle:
    """ 
    Defines a rectangle by its width and height.
    """

    number_of_instances = 0  # Class variable to keep track of the number of Rectangle instances
    print_symbol = "#"  # Class variable representing the print symbol for the rectangle

    def __init__(self, width=0, height=0):
        """ Initializes a new instance of the Rectangle class """
        self.width = width  # Set the width of the rectangle
        self.height = height  # Set the height of the rectangle
        Rectangle.number_of_instances += 1  # Increase the count of Rectangle instances

    def __str__(self):
        """ Returns a string representation of the rectangle """
        if self.width == 0 or self.height == 0:  # If width or height is 0, the rectangle does not exist
            return ""

        # Construct the string representation of the rectangle
        string = "\n".join(str(self.print_symbol) * self.width for _ in range(self.height))
        return string

    @property
    def width(self):
        """ Gets the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the rectangle, verifying it is an integer and not negative """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Gets the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the rectangle, verifying it is an integer and not negative """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Calculates and returns the area of the rectangle """
        return self.height * self.width

    def perimeter(self):
        """ Calculates and returns the perimeter of the rectangle """
        if self.width == 0 or self.height == 0:  # If width or height is 0, the rectangle does not exist
            return 0
        return 2 * (self.height + self.width)

    def __repr__(self):
        """ Returns a string that can be used to recreate the rectangle object """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """ Cleans up instance of Rectangle and reduces the count of Rectangle instances """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compares two Rectangle instances and returns the one with the larger (or equal) area """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ Creates a square (a special case of a rectangle) """
        return cls(size, size)
