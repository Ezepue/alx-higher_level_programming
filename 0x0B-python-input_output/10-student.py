#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiates Student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        if isinstance(attrs, list):
            result = {}
            for value in attrs:
                atb = getattr(self, value, None)
                if atb is None:
                    continue
                result[value] = atb
            return result
        return self.__dict__
