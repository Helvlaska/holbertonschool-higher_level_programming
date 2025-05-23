#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix
by a given number. All results are rounded to 2 decimal places as float.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns
    floats rounded to 2 decimals.
    """

    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    for row in matrix:
        for el in row:
            if not isinstance(el, (int, float)) or isinstance(el, bool):
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats"
                )
    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[float("{:.2f}".format(el / div)) for el in row] for row in matrix]
