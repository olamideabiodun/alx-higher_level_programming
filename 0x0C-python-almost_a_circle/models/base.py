#!/usr/bin/python3
"""Defines a Base model class"""


class Base:
    """Base Model"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
