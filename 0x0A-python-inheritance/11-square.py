#!/usr/bin/python3
"""Module that defines a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines square based on Rectangle"""

    def __init__(self, size):
        """Instantiates BaseGeometry object"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns printable representation of Rectangle"""

        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string
