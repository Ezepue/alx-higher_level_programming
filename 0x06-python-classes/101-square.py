#!/usr/bin/python3
"""Defines new square"""


class Square:
    """ An empty class that defines a Square

    Attributes:
    __size (int): Size of square. Size must be at least 0
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Instantiates new square

        Args:
            size (int): Size of square
            position (int, int): Where square will be printed
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Returns the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets new value to size

        Args:
            value: New value
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Retrieves position """
        return self.__position

    @position.setter
    def position(self, value):
        if (
            len(value) != 2
            or not isinstance(value, tuple)
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0 or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Calculates the area of square

        Args:
            self: Instance of square

        Return:
            Area of square size
        """
        return self.__size ** 2

    def my_print(self):
        """ Prints square
        """
        if self.__size == 0:
            print()
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")

    def __str__(self):
        """Makes square printable"""
        if self.__size == 0:
            return ""
        else:
            for i in range(0, self.__position[1]):
                print("")
            for i in range(0, self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size, end='')
                if i != self.__size - 1:
                    print("")
            return ""
