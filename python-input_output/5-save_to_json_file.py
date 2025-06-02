#!/usr/bin/python3
"""
Module 5-save_to_json_file
Writes a Python object to a file using its JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes a Python object to a text file using JSON format.

    Args:
        my_obj: The Python object to serialize.
        filename (str): The name of the file where the object will be saved.

    Note:
        - Uses the built-in 'json' module and the 'with' statement.
        - Overwrites the file if it already exists.
        - Does not return anything.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
