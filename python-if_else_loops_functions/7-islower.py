def islower(c):
    # on récupère la valeur ASCII du caractère c
    ascii_value = ord(c)

    # on définit les bornes pour les lettres minuscules
    min_lower = ord('a')
    max_lower = ord('z')

    # on vérifie si la valeur ASCII du caractère c est dans l'intervalle des minuscules
    if ascii_value >= min_lower and ascii_value <= max_lower:
        return True  # si oui, c'est une lettre minuscule
    else:
        return False  # sinon, ce n'est pas une lettre minuscule
