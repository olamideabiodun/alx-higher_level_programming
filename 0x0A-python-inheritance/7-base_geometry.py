#!/usr/bin/python3
"""based on Base-geometry class"""


class BaseGeometry:
    """A base_geometry class"""
    def area(self):
        raise Exception("area() is not implemented")
    pass

    def integer_validator(self, name, value):
        """integer validator"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
