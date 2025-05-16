#!/usr/bin/python3

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
    for char in text:
        buffer += char
        if char in ".?:":  # On a atteint une ponctuation à traiter
            print(buffer.strip())  # on nettoie les espaces autour
            print()
            print()
            buffer = ""  # On vide le buffer

    if buffer.strip():  # S'il reste quelque chose sans ponctuation finale
        print(buffer.strip())
