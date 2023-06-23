#!/usr/bin/python3
"""function that block the creation of new attr"""


class LockedClass:
    def __init__(self):
        super().__setattr__("first_name", "")

    def __setattr__(self, attribute, value):
        if attribute not in self.__dict__:
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")

        else:
            super().__setattr__(attribute, value)
