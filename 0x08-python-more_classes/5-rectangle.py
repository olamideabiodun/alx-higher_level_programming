#!/usr/bin/python3
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

    def __str__(self):
        """Return the str representation of the rectangle class"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rec = []
        for i in range(self.__height):
            [rec.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rec.append("\n")
        return ("". join(rec))

    def __repr__(self):
        """returns the repr of the rectangle"""
        return f"Rectangle(width = {self.__width}, height = {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        pass
