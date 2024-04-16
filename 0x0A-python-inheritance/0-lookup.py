#!/usr/bin/python3

"""Module defines a lookup function"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    return dir(obj)
