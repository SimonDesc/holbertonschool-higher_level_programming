#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    found = False
    for element in a_dictionary:
        if (element == key):
            a_dictionary[element] = value
            found = True
    if found is False:
        a_dictionary[key] = value
    return a_dictionary
