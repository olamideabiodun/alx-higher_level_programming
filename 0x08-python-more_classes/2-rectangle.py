#!/usr/bin/pytho3
"""Defines a rectangle class"""


class Rectangle:
    """This is a rectangle class"""
    def __init__(self, width=0, height=0):
        """INitializes the rectangle """

        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @width.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Defines the area"""
        return self.width * self.height

    def perimeter(self):
        """defines the perimeter"""
        if self.width == 0 or self.height == 0:
            return (0)
        return (2 * (self.width + self.height))
