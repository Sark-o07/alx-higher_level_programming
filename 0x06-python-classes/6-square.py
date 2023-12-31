#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size, position=(0, 0)):
        """
        Initializes a new Square instance with the given size

        Args:
            size (int): the size of the square's side.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """get/set current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(num, int) for num in value)
                or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
