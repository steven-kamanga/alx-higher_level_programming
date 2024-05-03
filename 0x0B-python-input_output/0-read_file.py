#!/usr/bin/python3
""" A module to read a UTF text file """


def read_file(filename=""):
    """ A method to read a text file (UTF8) and print it to stdout """
    with open(filename, encoding='utf-8') as f:
        text = f.read()
        print(text, end='')
