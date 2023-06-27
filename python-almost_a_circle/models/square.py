#!/usr/bin/python3
"""class Square that inherits from Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Define a Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """return the string of the square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """Setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.width = value
            self.height = value

    def update(self, *args, **kwargs):
        """update the args of rectangle"""
        if not kwargs:
            count = 0
            for arg in args:
                if count == 0:
                    self.id = arg
                if count == 1:
                    self.size = arg
                if count == 2:
                    self.x = arg
                if count == 3:
                    self.y = arg
                count += 1
        else:
            for cle, valeur in kwargs.items():
                if cle == "id":
                    self.id = valeur
                if cle == "size":
                    self.size = valeur
                if cle == "x":
                    self.x = valeur
                if cle == "y":
                    self.y = valeur
