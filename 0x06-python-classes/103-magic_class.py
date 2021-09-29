#!/usr/bin/python3
import math

'''comment'''
class MagicClass:
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
    '''comment'''
    def area(self, radius):
        return self.__radius ** 2 * math.pi
    '''comment'''
    def circumference(self, radius):
        return 2 * math.pi * self.__radius
