#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return
    max = 0
    current = 0
    for i in range(len(my_list)):
        current = my_list[i]
        if (current > max):
            max = my_list[i]
    return max
