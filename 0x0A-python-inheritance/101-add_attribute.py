#!/usr/bin/python3
"""Insertion module"""


def add_attribute(obj, attr, value):
    """
    Function that adds a new attribute to an object if it’s possible
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
