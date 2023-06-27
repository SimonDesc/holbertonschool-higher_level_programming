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
