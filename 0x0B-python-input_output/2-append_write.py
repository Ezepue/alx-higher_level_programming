#!/usr/bin/python3
"""Module containing function that writes to file"""


def append_write(filename="", text=""):
    """Function that writes to file.
    Args:
        filename (file): File for writing
        text (str): Text to be written to file
    """
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
