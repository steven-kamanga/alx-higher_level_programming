#!/usr/bin/python3


"""Module defines a function thath returns True is the obj is exactly an instance of the specified class else
that inherited from the specified class, otherwise False"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class or inherited from the specified class
    Args:
        obj: object to check
        a_class: class to check against
    Returns:
        True if object is an instance of class or inherited from the specified class, otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False
