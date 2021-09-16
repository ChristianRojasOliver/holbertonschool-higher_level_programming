#!/usr/bin/python3
def uniq_add(my_list=[]):
    add_int = list(set(my_list))
    result = 0
    for i in range(len(add_int)):
        result = result + add_int[i]
    return result
