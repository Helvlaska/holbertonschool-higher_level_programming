#!/usr/bin/python3
""" Création d'une classe avec:
- Une méthode area() qui renvoie un message d'erreur
- Une méthode integer_validator() pour valider des entier positifs
"""


class BaseGeometry():
    """ Création d'une classe avec:
    - Une méthode area() qui renvoie un message d'erreur
    - Une méthode integer_validator() pour valider des entier positifs
    """
    def area(self):
        """
        Méthode non implémentée par défaut.
        Lève une exception pour indiquer que le calcul d'aire n'est pas
        encore défini.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide que `value` est un entier strictement positif.

        Args:
            name (str): Le nom de l'attribut (utilisé dans
            les messages d'erreur).
            value (int): La valeur à valider.

        Raises:
            TypeError: Si `value` n'est pas un entier.
            ValueError: Si `value` est inférieur ou égal à 0.
        """
        self.name = name
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{self.name} must be greater than 0")
        else:
            self.value = value
