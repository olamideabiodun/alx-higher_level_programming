#!/usr/bin/python3
def safe_print_integer(value):
    """
    Prints the given integer value, but only if it is a valid number.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
