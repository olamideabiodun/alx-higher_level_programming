#!usr/bin/python3
"""Function that adds integers"""


def add_integer(a, b=98):
    """adds two integers"""
    if not isinstance(a, float) and not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, float) and not isinstance(b, int):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = float(a)
    elif isinstance(a, int):
        a = int(a)
    if isinstance(b, float):
        b = float(b)
    elif isinstance(b, int):
        b = int(b)

    sum = a + b
    return sum
