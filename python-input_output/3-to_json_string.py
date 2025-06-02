#!/usr/bin/python3
"""Converts a Python object to a JSON string.
"""
import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON-formatted string.

    Args:
        my_obj: The Python object to convert (e.g. dict, list, str, int, bool).

    Returns:
        str: A string containing the JSON representation of the object.

    Note:
        - Uses the built-in 'json' module.
        - No exception handling is required if the object is not serializable.
    """
    return json.dumps(my_obj)
