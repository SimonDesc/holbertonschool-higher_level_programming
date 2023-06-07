#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    winner = None
    if a_dictionary is None:
        return winner
    for element in a_dictionary:
        if a_dictionary[element] > max:
            max = a_dictionary[element]
            winner = element
    return (winner)
