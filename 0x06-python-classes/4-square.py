#!/usr/bin/python3
"""Defines a square"""


class Square:
    """ An empty class that defines a Square

    Attributes:
        __size (int): Size of square. Size must be at least 0
    """
    def __init__(self, size=0):
        """init method

        Args:
            size (int): Size of Square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ Returns the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Calculates the area of square

        Args:
            self: Instance of square

        Return:
            Area of square size
        """
        return (self.__size * self.__size)
