#!/usr/bin/python3
"""
Module 0-read_file
Reads and prints the content of a text file (UTF8) to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The path to the text file (default is "").

    Note:
        - The file is opened using a 'with' statement to ensure proper closure.
        - The file content is printed without an additional newline.
        - File permissions or exceptions do not need to be handled.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
