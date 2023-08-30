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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: the area of the square.
        """
        return self.__size ** 2
