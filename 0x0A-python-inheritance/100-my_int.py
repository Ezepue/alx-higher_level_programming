#!/usr/bin/python3
"""Module for MyInt class"""


class MyInt(int):
    """MyInt class"""

    def __init__(self, number):
        """Initializes object"""
        self.number = number

    def __eq__(self, other):
        """Inverts == operator"""
        return self.number != other

    def __ne__(self, other):
        """Inverts != operator"""
        return self.number == other
