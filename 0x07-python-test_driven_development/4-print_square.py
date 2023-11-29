#!usr/bin/python3
"""A function that prints a square"""


def print_square(size):
    """prints # in range of size
    
    size must be int else raise TypeError
    
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
