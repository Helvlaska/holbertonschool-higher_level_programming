#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = []

    for ligne in matrix:
        new_ligne = []
        for value in ligne:
            new_ligne.append(value ** 2)
        new_matrix.append(new_ligne)

    return new_matrix
