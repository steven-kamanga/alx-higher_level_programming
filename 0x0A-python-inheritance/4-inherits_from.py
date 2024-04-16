#!/usr/bin/python3

"""
    Module defines a function that returns True if the object is an instance of a class that inherited
    from the specified class, otherwise False
"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited from the specified class
    Args:
        obj: object to check
        a_class: class to check against
    Returns:
        True if object is an instance of class that inherited from the specified class, otherwise False
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
