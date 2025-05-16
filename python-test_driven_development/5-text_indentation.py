#!/usr/bin/python3
"""This module provides text_indentation."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The text to process.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    i = 0

    while i < len(text):
        char = text[i]

        if char in ".?:":
            # Supprimer les espaces à droite avant d'ajouter la ponctuation
            buffer = buffer.rstrip()
            buffer += char

            # Ajouter les ponctuations successives si elles suivent directement
            while i + 1 < len(text) and text[i + 1] in ".?:":
                i += 1
                buffer += text[i]

            # Affichage du bloc nettoyé
            print(buffer.strip())
            print()
            print()
            buffer = ""  # Réinitialiser le buffer après impression
        else:
            buffer += char

        i += 1

    # Si du texte reste après la dernière ponctuation
    if buffer.strip():
        print(buffer.strip())
