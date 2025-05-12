#!/usr/bin/python3

def no_c(my_string):
    
    string = ""
    
    for i in my_string:
        valeur_ascii = ord(i)
        if valeur_ascii == 99 or valeur_ascii == 67:
            continue
        else:
            string += (i)
    return string
