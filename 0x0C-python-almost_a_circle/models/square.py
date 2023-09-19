#!/usr/bin/python3
"""The Square Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """the Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initiates the class instance"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Module size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Module size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """"returns formatted string desc of the square instance"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)

    def update(self, *args, **kwargs):
        """updates the attributes of the class instance"""
        if len(args) == 0:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)
            return
        else:
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.size = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg

    def to_dictionary(self):
        """Returns the dict rep of a Square instance"""
        return {
                "id": self.id,
                "size": self.size,
                "x": self.x,
                "y": self.y
                }
