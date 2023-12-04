#!/usr/bin/python3
"""Prints list in sorted order"""


class MyList(list):
    """Inherits from list function"""
    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints in assending order"""
        print(sorted(self))
