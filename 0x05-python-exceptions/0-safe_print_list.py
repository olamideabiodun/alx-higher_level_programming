#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """print elemnt x of a list
    Args:
    my_list (list, optional) : the list to print. Defaults to [].
    x (int, optional) : index in the list. Defaults to 0.

    Returns:
    x element of my_list
    """
    ret = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
