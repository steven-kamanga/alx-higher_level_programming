#!/usr/bin/python3
"""Module for matrix_mul function"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices
    Args:
        m_a (list): first matrix
        m_b (list): second matrix
    Raises:
        TypeError: if m_a or m_b are not lists
        TypeError: if m_a or m_b are not lists of lists
        TypeError: if m_a or m_b contain non-integer or non-float elements
        ValueError: if m_a or m_b are empty
        ValueError: if m_a or m_b are not rectangular
        ValueError: if m_a and m_b can't be multiplied
    Returns:
        A new matrix representing the multiplication of m_a and m_b
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    if not all(type(row) is list for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(type(row) is list for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not all(all(type(ele) is int or type(ele) is float for ele in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(type(ele) is int or type(ele) is float for ele in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise ValueError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = []
    for row in m_a:
        new_row = []
        for col in range(len(m_b[0])):
            new_row.append(sum([row[i] * m_b[i][col]
                           for i in range(len(row))]))
        inverted_b.append(new_row)

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in range(len(m_b[0])):
            new_row.append(sum([row[i] * m_b[i][col]
                           for i in range(len(row))]))
        new_matrix.append(new_row)

    return new_matrix
