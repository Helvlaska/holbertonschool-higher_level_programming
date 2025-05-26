#!/usr/bin/python3
""" Création d'une classe enfant qui permet de :
    - Récupérer une liste (parent)
    - trier la liste de façon croissante
    - print la liste triée
"""


class MyList(list):
    """
    Classe qui hérite de la classe list.

    Fournit une méthode supplémentaire `print_sorted()` qui affiche
    les éléments de la liste triés par ordre croissant, sans modifier
    l'ordre original de la liste.
    """
    def print_sorted(self):
        """
        Affiche les éléments de la liste triés dans l'ordre croissant.

        Cette méthode n'altère pas la liste d'origine.
        """
        print(sorted(self))
