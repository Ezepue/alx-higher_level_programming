#!/usr/bin/python3
"""Module that defines a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines square based on Rectangle"""

    def __init__(self, size):
        """Instantiates square object"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
