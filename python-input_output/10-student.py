#!/usr/bin/python3
"""
Module 9-student
Définit une classe Student avec des attributs publics et une méthode
permettant de récupérer un dictionnaire prêt à être sérialisé en JSON.
"""
import sys


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

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire représentant les attributs de l'étudiant.

        Si attrs est une liste de chaînes de caractères, seules les clés
        listées présentes dans l’objet sont retournées.

        Sinon, tous les attributs publics de l’objet sont retournés.

        Returns:
            dict: Les attributs de l'instance, filtrés si nécessaire.
        """
        # vérifie que tous les item de la liste sont des chaînes de caractères
        if isinstance(attrs, list):
            is_string = True # initialise le booleen à true
            for element in attrs: # ont boucle sur la liste d'attributs                
                if not isinstance(element, str): # si l'item n'est pas une string
                    is_string = False # booleen à false
                    break # sortie de la boucle
        
            # Si attrs est une liste et que tous ses éléments sont des chaînes
            if is_string: # si le booleen est true
                dictionnaire_filtré = {} # créer un dictionnaire vide
                for key in attrs: # boucle sur la liste
                    if key in self.__dict__: # si la key est dans la liste d'attribut
                        valeur = self.__dict__[key] # on récupère la valeur de la clef
                        dictionnaire_filtré[key] = valeur # on ajoute la paire cle/valeur
                return dictionnaire_filtré # on retourne le dictionnaire

        # Si attrs est None ou pas une liste valide → on retourne tous les attributs
        return self.__dict__
