#!/usr/bin/env python3
"""
Module task_01_pickle

Ce module définit une classe CustomObject avec des méthodes de
sérialisation et désérialisation utilisant le module `pickle`.

Fonctionnalités :
- Sérialiser une instance de CustomObject dans un fichier binaire.
- Désérialiser un fichier pour recréer une instance de CustomObject.
- Afficher les attributs d'un objet de manière lisible.

Attention : la désérialisation avec pickle doit toujours être faite
à partir de sources sûres.
"""
import pickle


class CustomObject():
    def __init__(self, name, age, is_student):
        """
        Initialise un objet CustomObject.

        Args:
            name (str): Le nom de la personne.
            age (int): L'âge de la personne.
            is_student (bool): Indique si la personne est étudiante.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les attributs de l'objet de manière lisible.
        """
        print(f"Nom: {self.name}")
        print(f"Age: {self.age}")
        print(f"Est étudiant: {self.is_student}")

    def serialize(self, filename):
        """
        Sérialise l’objet dans un fichier binaire avec Pickle.

        Args:
            filename (str): Le chemin du fichier de sortie.

        Exceptions:
            Affiche une erreur si l’écriture échoue.
        """
        # Sérialisation dans un fichier binaire
        with open(filename, "wb") as file:
            # Pareil que json mais avec pickle
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise un objet CustomObject depuis un fichier.

        Args:
            filename (str): Le chemin du fichier à charger.

        Returns:
            CustomObject | None: L’objet désérialisé ou None en cas d’erreur.

        Exceptions:
            Gère les erreurs de lecture, d’absence de fichier,
            ou d’objet invalide.
        """
        try:  # J'essaie d'ouvrir le fichier
            with open(filename, "rb") as file:
                # Je récupère l'objet
                obj = pickle.load(file)
                # Je vérifie que obj est bien une instance de la classe
                if isinstance(obj, cls):
                    return obj  # Si oui je retourne l'objet
        # Sinon soulève une exception avec message erreur
        except (FileNotFoundError, pickle.UnpicklingError,
                EOFError, IOError) as e:
            print(f"Erreur lors de la désérialisation : {e}")
        return None  # Ont return None
