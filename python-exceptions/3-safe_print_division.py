#!/usr/bin/python3
def safe_print_list_integers(a, b):
    sum = 0
    try:
        sum = a / b
        return sum
    except ZeroDivisionError:
        sum = None
    finally:
        print("Inside result: {}".format(sum))
