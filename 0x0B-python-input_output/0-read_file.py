#!/usr/bin/python3
"""A function that reads a text file"""


def read_file(filename=""):
    """Print the content of a UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
