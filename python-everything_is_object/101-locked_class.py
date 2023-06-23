#!/usr/bin/python3
"""function that block the creation of new attr"""


class LockedClass:
    """block only to first name"""

    __slots__ = ["first_name"]
