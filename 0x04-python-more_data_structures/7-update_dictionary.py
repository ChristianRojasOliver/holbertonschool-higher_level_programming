#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_key = 0
    for oldKey in a_dictionary:
        if oldKey == key:
            a_dictionary[oldKey] = value
            new_key = 1
    if new_key == 0:
        a_dictionary[key] = value
    return a_dictionary
