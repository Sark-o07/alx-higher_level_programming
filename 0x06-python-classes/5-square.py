#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

	    def __init__(self, size=0):
        """
        Initializes a new Square instance with the given size

        Args:
            size (int): the size of the square's side.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(0, self.__size)]
            print("")
        if self.__size == 0:
            print("")
