#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a number.
All divisions are rounded to 2 decimal places.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The divisor (non-zero).

    Returns:
        list of lists: New matrix with all elements divided by div.

    Raises:
        TypeError: If matrix is not a matrix of int/float, or div is not a number.
        TypeError: If matrix rows are not all the same size.
        ZeroDivisionError: If div is 0.
    """

    # Vérification de la structure principale de la matrice
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if any(len(row) == 0 for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Vérification que tous les éléments sont int/float, et que toutes les lignes sont de même taille
    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)) or isinstance(element, bool):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Vérification du diviseur
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Retour de la nouvelle matrice divisée et arrondie
    return [[round(element / div, 2) for element in row] for row in matrix]
