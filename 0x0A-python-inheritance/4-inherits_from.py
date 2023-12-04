#!/usr/bin/python3
"""Sub-class or not"""


def inherits_from(obj, a_class):
    """Chcks if issubclass"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
