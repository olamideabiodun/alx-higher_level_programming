#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Add an item to a list at the given index.
    If there is already something in that position it will be replaced."""
    # TODO: Implement this function!
    copy = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        copy[idx] = element
        return copy
