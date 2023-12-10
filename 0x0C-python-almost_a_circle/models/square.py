#!/usr/bin/python3
"""Module containing Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates Square object"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute:

        1st argument should be the id attribute
        2nd argument should be the size attribute
        3rd argument should be the x attribute
        4th argument should be the y attribute
        """
        if args:
            length = len(args)
            if length >= 1:
                self.id = args[0]
            if length >= 2:
                self.size = args[1]
            if length >= 3:
                self.x = args[2]
            if length >= 4:
                self.y = args[3]
        elif kwargs:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.size = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def __str__(self):
        """
        Return the print() and str() representation of a Square.
        """
        string = ""
        string += f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
        return string

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square.
        """
        result = {}
        result.update({'id': self.id, 'size': self.size})
        result.update({'x': self.x, 'y': self.y})
        return result

    def to_list(self):
        """
        Returns list representation of Square
        """
        return [self.id, self.size, self.x, self.y]
