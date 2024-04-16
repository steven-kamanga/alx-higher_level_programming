#!/usr/bin/python3

"Module defines a class to check if an object is an instance of a class"


def is_same_class(obj, a_class):
    """Checks is an object is an instance of a class
    Args:
        obj: object to check
        a_class: class to check against
    Returns:
        True if object is an instance of class, otherwise False
    """
    if obj.__class__ == a_class:
        return True
    return False
