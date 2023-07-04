#!/usr/bin/python3
"""Defin  matrix multiplication function BY NumPy."""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """return mltuplication  two matrices.

    Args:
        m_a (list of lsts of ints/floats): 1 matrix.
        m_b (list of lsts of ints/floats):2 matrix.
    """

    return (np.matmul(m_a, m_b))
