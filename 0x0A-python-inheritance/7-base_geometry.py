#!/usr/bin/python3
"""Module that defines a BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises Exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""

        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
