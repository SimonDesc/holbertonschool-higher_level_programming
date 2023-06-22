#!/usr/bin/python3
'''student to JSON'''


class Student:
    '''class student'''

    def __init__(self, first_name, last_name, age):
        '''class student with attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''horrible'''
        if attrs is None:
            return self.__dict__
        else:
            dict = {key: self.__dict__[key] for key in attrs
                    if key in self.__dict__}
            return dict

    def reload_from_json(self, json):
        '''reload from json'''
        for key in json:
            if key in self.__dict__:
                self.__dict__[key] = json[key]
