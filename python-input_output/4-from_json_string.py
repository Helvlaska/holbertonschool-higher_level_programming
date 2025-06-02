#!/usr/bin/python3
"""
Module 4-from_json_string
Returns a Python object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Converts a JSON-formatted string to a corresponding Python object.

    Args:
        my_str (str): A string containing a valid JSON representation.

    Returns:
        object: The Python data structure represented by the JSON string
                (e.g. dict, list, int, str, etc.).

    Note:
        - Uses the built-in 'json' module.
        - No exception handling is required for invalid JSON.
    """
    return json.loads(my_str)
