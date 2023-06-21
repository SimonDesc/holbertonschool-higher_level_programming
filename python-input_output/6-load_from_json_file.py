#!/usr/bin/python3
"""creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """create an objet from a json file"""
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)
        return data
