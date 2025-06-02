#!/usr/bin/python3
"""
Module 2-append_write
Appends a string at the end of a text file (UTF8) and
returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8) and
    returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters written.

    Note:
        - Creates the file if it does not exist.
        - Appends text without erasing existing content.
        - Uses a 'with' statement to ensure the file is properly closed.
        - No exception handling is required.
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
