#!/usr/bin/python3
""" square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """Inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """bob construye"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns formatted information display"""

        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)
