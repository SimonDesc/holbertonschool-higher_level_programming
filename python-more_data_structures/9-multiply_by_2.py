#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionnary = {}
    for element in a_dictionary:
        new_dictionnary[element] = a_dictionary[element]*2
    return new_dictionnary
