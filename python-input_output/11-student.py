#!/usr/bin/python3
"""
Module 11-student
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
            is_string = True
            for element in attrs:
                if not isinstance(element, str):
                    is_string = False
                    break

            # Si attrs est une liste et que tous ses éléments sont des chaînes
            if is_string:
                dictionnaire_filtré = {}
                for key in attrs:
                    if key in self.__dict__:
                        valeur = self.__dict__[key]
                        dictionnaire_filtré[key] = valeur
                return dictionnaire_filtré
        return self.__dict__

    def reload_from_json(self, json):
        """
        Remplace les attributs de l'objet par ceux fournis
        dans un dictionnaire.

        Cette méthode met à jour les attributs de l'instance
        Student en utilisant les paires clé/valeur du dictionnaire
        passé en paramètre. Si une clé ne correspond pas à un
        attribut existant, elle sera ajoutée comme nouvel attribut.

        Args:
            json (dict): Un dictionnaire contenant les nouvelles
            valeurs d'attributs.
        """
        for key in json:
            setattr(self, key, json[key])
            # modifie ou crée l'attribut
            # avec la nouvelle valeur
