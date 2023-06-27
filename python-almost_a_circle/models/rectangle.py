#!/usr/bin/python3
"""class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Return informations on the Rectangle"""
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
            f" - {self.__width}/{self.__height}"
        )

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for heigth"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Return the area"""
        return self.__width * self.__height

    def display(self):
        """Display a Rectangle"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """update the args of rectangle"""
        if kwargs is None:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                if count == 1:
                    self.__width = arg
                if count == 2:
                    self.__height = arg
                if count == 3:
                    self.__x = arg
                if count == 4:
                    self.__y = arg
                count += 1
        else:
            for cle, valeur in kwargs.items():
                if cle == "id":
                    self.id = valeur
                if cle == "width":
                    self.__width = valeur
                if cle == "height":
                    self.__height = valeur
                if cle == "x":
                    self.__x = valeur
                if cle == "y":
                    self.__y = valeur

    def to_dictionary(self):
        """return the dictionary representation"""
        return {
            "x": self.x,
            "y": self.y,
            "id": self.id,
            "height": self.height,
            "width": self.width,
        }
