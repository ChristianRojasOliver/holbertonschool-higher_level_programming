#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary is None or a_dictionary == {}:
        return None
    new_key = 1
    for key in a_dictionary:
        if new_key == 1:
            largestVal = a_dictionary[key]
            largestKey = key
            new_key = 0
        if a_dictionary[key] > largestVal:
            largestVal = a_dictionary[key]
            largestKey = key
    return largestKey
