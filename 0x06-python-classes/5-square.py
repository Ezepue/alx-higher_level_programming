#!/usr/bin/python3

"""Defines a square"""


class Square:
    """An empty class that defines a Square.

    Attributes:
        size (int): Size of square
    """

    def __init__(self, size=0):
        """Instantiates new square.

        Args:
            size (int): Size of square.
        """
        self.size = size

    @property
    def size(self):
        """Returns the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of square."""
        return self.__size ** 2

    def my_print(self):
        """Prints square with "#" character"""
        if self.__size == 0:
            print("")
            return
        for _ in range(self.__size):
            print("#" * self.__size)
