#!/usr/bin/python3
"""Adds two integers"""


def add_integer(a, b=98):
    """Function that adds integers"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    sum = a + b
    return sum
