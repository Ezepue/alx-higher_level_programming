#!/usr/bin/python3
"""Module containing function that reads file"""


def read_file(filename=""):
    """Function that reads file"""

    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end="")
