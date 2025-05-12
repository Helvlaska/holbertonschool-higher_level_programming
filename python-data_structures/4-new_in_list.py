#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    b = my_list.copy() #copie de la liste originale
    if idx < 0 or idx >= len(b):
        return my_list
    
    b[idx] = element
    return b
