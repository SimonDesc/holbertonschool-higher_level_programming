#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    if roman_string is None or not isinstance(roman_string, str):
        return int_val
    for i in range(len(roman_string)):
        current_val = rom_val[roman_string[i]]
        if i > 0:
            previous_val = rom_val[roman_string[i - 1]]
            if current_val > previous_val:
                int_val += current_val - 2 * previous_val
            else:
                int_val += current_val
        else:
            int_val += current_val
    return int_val
