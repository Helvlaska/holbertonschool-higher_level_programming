#!/usr/bin/python3
"""
Module 9-student
Définit une classe Student avec des attributs publics et une méthode
permettant de récupérer un dictionnaire prêt à être sérialisé en JSON.
"""


class Student():
    """
    Représente un étudiant avec un prénom, un nom de famille et un âge.

    Attributs publics :
        - first_name (str) : prénom
        - last_name (str) : nom de famille
        - age (int) : âge de l’étudiant
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialise une nouvelle instance de Student.

        Args:
            first_name (str): Le prénom de l'étudiant.
            last_name (str): Le nom de famille de l'étudiant.
            age (int): L'âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retourne un dictionnaire contenant les attributs de l'étudiant.

        Ce dictionnaire peut être utilisé directement pour une sérialisation.

        Returns:
            dict: Les attributs de l'instance sous forme clé/valeur.
        """
        return self.__dict__
