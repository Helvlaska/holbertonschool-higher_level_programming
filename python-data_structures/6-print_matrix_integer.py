#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for ligne in matrix:
        i = 0
        while i < len(ligne):
            print("{:d}".format(ligne[i]), end="")
            if i != len(ligne) - 1:
                print(" ", end="")
            i += 1
        print()

