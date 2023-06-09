#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for element in range(list_length):
        try:
            new_list.append(my_list_1[element] / my_list_2[element])
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)
        except TypeError:
            print("wrong type")
            new_list.append(0)
        except IndexError:
            print("out of range")
            new_list.append(0)
    return new_list
