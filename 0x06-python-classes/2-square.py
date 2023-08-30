#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""


def __init__(self, size):
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
