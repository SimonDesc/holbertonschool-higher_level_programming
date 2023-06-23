#!/usr/bin/python3
"""a class that invert == and !="""


class MyInt(int):
    """invert the two operand with dunder method"""

    def __eq__(self, other):
        if isinstance(self, type(other)):
            return False
        return True

    def __ne__(self, other):
        if isinstance(self, type(other)):
            return True
        return False
