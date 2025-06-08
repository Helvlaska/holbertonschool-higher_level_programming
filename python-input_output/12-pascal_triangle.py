#!/usr/bin/python3
"""
Module 12-pascal_triangle
Contient une fonction permettant de générer les n premières
lignes du triangle de Pascal.
"""


def pascal_triangle(n):
    """
    Génère les n premières lignes du triangle de Pascal.

    Args:
        n (int): Le nombre de lignes à générer.

    Returns:
        list: Une liste de listes représentant le triangle de Pascal.
    """
    # Cas de base : n nul ou négatif → on retourne une liste vide
    if n <= 0:
        return []
    # Initialise le triangle comme une liste vide
    triangle = []

    for l_idx in range(n):  # Pour chaque ligne à construire
        ligne = []  # On crée une nouvelle ligne vide
        # Le nombre d'éléments dans chaque ligne augmente à chaque fois
        for i in range(l_idx + 1):
            if i == 0 or i == l_idx:
                # Les premiers et derniers éléments sont toujours 1
                ligne.append(1)
            else:
                # Somme des deux éléments au-dessus dans la ligne précédente
                valeur = triangle[l_idx - 1][i - 1] + triangle[l_idx - 1][i]
                ligne.append(valeur)

        triangle.append(ligne)  # Ajoute la ligne construite au triangle

    return triangle
