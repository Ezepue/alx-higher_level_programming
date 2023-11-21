#!/usr/bin/python3
"""Defines a square"""


class Square:
    """ An empty class that defines a Square

    Attributes:
        __size (int): Size of square. Size must be at least 0
    """
    def __init__(self, size=0):
        """Init method

        Args:
            size (int): Size of square
        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
