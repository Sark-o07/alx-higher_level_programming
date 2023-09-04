#!/usr/bin/python3
"""Module 2-rectangle
Defines a Rectangle class with area
and perimeter
"""


class Rectangle:
    """Rectangle with defined width and height"""
    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.

        Args:
            width: width of the rectangle
            height: height of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of a Rectangle instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance

        Args:
            value: value of the width, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance

        Args:
            value: value of the height, must be a positive integer
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a Rectangle instance

        Returns:
            Area = width * height
        """
        return self.__width * self.__height

    def height(self):
        """Calculates the perimeter of a Rectangle instance

        Returns:
            Perimeter = 2 * (height + width)
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
