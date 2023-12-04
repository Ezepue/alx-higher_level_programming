#!/usr/bin/python3
"""
Module that checks if specified object is a subclass of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Module that checks if specified object is a
    subclass of a specified class.
    """

    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
