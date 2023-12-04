#!/usr/bin/python3
"""Checks if isinstance"""


def is_same_class(obj, a_class):
    """returns true if isinstance"""
    if type(obj) == a_class:
        return True
    return False
