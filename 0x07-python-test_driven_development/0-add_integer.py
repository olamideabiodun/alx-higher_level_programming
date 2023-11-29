#!usr/bin/python3
"""Function that adds integers"""


def add_integer(a, b=98):

    """raises error if a is not a float or integer"""
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")

    """raises error if b is not a float or integer"""
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")

    """adds a as float if its a float elif its an in, add as int"""
    if isinstance(a, float):
        a = float(a)
    elif isinstance(a, int):
        a = int(a)

    """adds b as float if its a float elif its an int add as int"""
    if isinstance(b, float):
        b = float(b)
    elif isinstance(b, int):
        b = int(b)
    
    """adds a and b"""
    sum = a + b
    return sum
