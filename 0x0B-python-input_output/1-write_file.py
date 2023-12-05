#!/usr/bin/python3
"""Module containing function that writes to file"""


def write_file(filename="", text=""):
    """Function that writes to file.
    Args:
        filename (file): File for writing
        text (str): Text to be written to file
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
