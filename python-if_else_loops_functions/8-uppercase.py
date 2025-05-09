#!/usr/bin/python3

def uppercase(str):
    # Créer une variable vide pour accumuler les résultats modifiés
    upper_string = ""

    # Boucle sur chaque caractère de la chaîne d'entrée
    for char in str:
        # On récupère la valeur ASCII du caractère actuel
        ascii_value = ord(char)

        # Vérification si le caractère est une lettre minuscule
        if ascii_value >= ord('a') and ascii_value <= ord('z'):
            # Si c'est une lettre minuscule, on la convertit en majuscule
            # En soustrayant 32 de la valeur ASCII
            new_char = chr(ascii_value - 32)

            # Ajouter le caractère modifié (majuscule) dans la string
            upper_string += new_char
        else:
            # Si ce n'est pas une lettre minuscule, on garde le char tel quel
            upper_string += char

    # Imprimer le résultat final sans retour à la ligne supplémentaire
    print("{}".format(upper_string))
