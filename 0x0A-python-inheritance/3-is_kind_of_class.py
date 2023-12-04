#!/usr/bin/python3
"""Checks if isinstance or inherited"""


def is_kind_of_class(obj, a_class):
    """True If isinstance else false"""
    if isinstance(obj, a_class):
        return True
    return False
