#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix
by a given number, rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div and returns a new matrix."""

    # Vérifie que matrix est une liste non vide
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    # Vérifie que chaque élément de matrix est une liste
    for row in matrix:
        if not isinstance(row, list):
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

    # Vérifie que toutes les lignes ont la même taille
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    # Vérifie que div est un int ou un float
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Vérifie que div est différent de 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Construction de la nouvelle matrice
    new_matrix = []
    for row in matrix:
        new_row = []
        for el in row:
            value = el / div
            value = int(value * 100 + 0.5) / 100
            new_row.append(value)
        new_matrix.append(new_row)

    return new_matrix
