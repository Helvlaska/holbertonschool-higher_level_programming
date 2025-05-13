#!/usr/bin/python3

def uniq_add(my_list=[]):
    delete_doublon = set(my_list)
    result = sum(delete_doublon)
    return result
