#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    ligne = ""
    for i in matrix:
        for j in i:
            ligne += "{} ".format(j)
        ligne += "\n"
    print("{}".format(ligne), end="")
