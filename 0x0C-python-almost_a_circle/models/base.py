#!/usr/bin/python3
"""Base Class"""


class Base:
    """Function"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

obj = Base(1)
cro = Base(2)
print(obj.id)
print(cro.id)
