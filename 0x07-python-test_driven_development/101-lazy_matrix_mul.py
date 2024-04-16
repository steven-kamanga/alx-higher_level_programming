#!/usr/bin/python3
import numpy as np

"""Module to multiply two matrices using numpy"""


def lazy_matrix_mul(m_a, m_b):
    """Function to multiply two matrices using numpy

    Args:
        m_a (list): first matrix
        m_b (list): second matrix

    Returns:
        A new matrix representing the multiplication of m_a and m_b
    """
    return np.matmul(m_a, m_b)
