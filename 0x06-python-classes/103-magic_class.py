#!/usr/bin/python3
import math'''comment'''


class MagicClass:
    def __init__(self, radius):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius
    '''commen'''
    def area(self, radius):
        return self.__radius ** 2 * math.pi
    '''commen'''
    def circumference(self, radius):
        return 2 * math.pi * self.__radius
