#!/usr/bin/python3
"""
Module 1-write_file
Writes a string to a text file (UTF8) and returns
the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8) and returns the number of
    characters written.

    Args:
        filename (str): The path to the file (default is an empty string).
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written.

    Note:
        - The file is created if it does not exist.
        - The content is overwritten if the file already exists.
        - The function uses a 'with' statement to handle file opening
        and closing.
        - No exception handling is required.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
