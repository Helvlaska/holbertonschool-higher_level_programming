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
            buffer = buffer.rstrip()
            buffer += char

            # Ajoute toutes les ponctuations qui suivent
            while i + 1 < len(text) and text[i + 1] in ".?:":
                i += 1
                buffer += text[i]

            # Affichage du bloc propre
            print(buffer.strip())
            print()
            print()
            buffer = ""  # Réinitialiser
        else:
            buffer += char

        i += 1

    if buffer.strip():
        print(buffer.strip())
