#!/usr/bin/python3
"""The Rectangle Module"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle
    inherits from:
        Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of the width"""
        self.setter_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value of the height"""
        self.setter_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """Returns the y coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the value of the x"""
        self.setter_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """Returns the x coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the value of the y"""
        self.setter_validator("y", value)
        self.__y = value

    @staticmethod
    def setter_validator(attr, value):
        if type(value) != int:
            raise TypeError(f"{attr} must be an integer")
        if attr == "x" or attr == "y":
            if value < 0:
                raise ValueError(f"{attr} must be >= 0")
        elif value <= 0:
            raise ValueError(f"{attr} must be > 0")

    def area(self):
        """Returns the Area of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """prints the Rectangle instance with the char '#'"""
        rectangle = ""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            rectangle += (" " * self.x) + ('#' * self.width) + "\n"
        print(rectangle, end="")

    def __str__(self):
        """returns a formatted string desc of the rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """Returns the dict rep of a Square instance"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
