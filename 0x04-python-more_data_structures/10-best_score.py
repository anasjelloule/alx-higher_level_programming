#!/usr/bin/python3
def best_score(a_dictionary):
    biggest = 0

    if not a_dictionary:
        return "None"

    for idx in a_dictionary:
        if a_dictionary[idx] > biggest:
            biggest = a_dictionary[idx]
            nm = idx

    return nm
