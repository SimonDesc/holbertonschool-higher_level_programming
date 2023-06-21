#!/usr/bin/python3
"""class to JSON"""


import json


def class_to_json(obj):
    """class to JSON"""
    return json.dumps(obj.__dict__)
