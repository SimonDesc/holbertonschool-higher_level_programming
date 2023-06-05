#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return
    new_string = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            new_string += ""
        else:
            new_string += i
    return (new_string)
