#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for key in a_dictionary:
        new_value = a_dictionary[key] * 2
        new_dictionary[key] = new_value
    return new_dictionary
