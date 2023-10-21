#!/usr/bin/python3
"""Defines a Rectangle Class"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class representing a square."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """sets the size of the new square"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
