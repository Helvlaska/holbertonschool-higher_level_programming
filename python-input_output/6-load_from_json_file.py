#!/usr/bin/python3
"""
Module 6-load_from_json_file
Loads a Python object from a file containing JSON data.
"""
import json


def load_from_json_file(filename):
    """
    Loads a Python object from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        object: The deserialized Python object.
    """
    with open(filename, "r") as f:
        return json.load(f)
