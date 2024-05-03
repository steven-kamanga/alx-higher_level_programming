#!/usr/bin/python3
""" A module that writes a string to a UTF8 text file """


def write_file(filename="", text=""):
    """ A method that writes a string to a text file (UTF8) and
    returns the number of characters written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
