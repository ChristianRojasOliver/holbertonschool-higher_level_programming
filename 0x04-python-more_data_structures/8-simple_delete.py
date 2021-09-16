#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new_key = 0
    for oldKey in a_dictionary:
        if oldKey == key:
            new_key = 1
    if new_key == 1:
        del a_dictionary[key]
    return a_dictionary
