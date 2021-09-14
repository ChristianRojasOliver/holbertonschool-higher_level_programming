#!/usr/bin/python3
def no_c(my_string):

    string_cpy = ""
    if (my_string is None):
        return None
    for i in my_string:
        if (i != 'c' and i != 'C'):
            string_cpy += i
    return string_cpy
