#!/usr/bin/python3
"""My list class"""


class MyList(list):
    """My List Class"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """Sort and print list of numbers"""
        print(sorted(self))
