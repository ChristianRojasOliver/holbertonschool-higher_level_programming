#!/usr/bin/python3
'''Module'''


class Square:
    '''comment'''
    def __init__(self, size=0):
        '''manipulando data'''
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
