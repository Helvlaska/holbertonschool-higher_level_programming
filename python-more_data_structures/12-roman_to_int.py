#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    result = 0
    dict_trad = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
    for i in range(len(roman_string)):
        char = roman_string[i]
        pr_char = roman_string[i - 1]
        if char in dict_trad:
            if i > 0 and pr_char == 'I' and (char == 'V' or char == 'X'):
                twist = dict_trad[char] - 2
                result = result + twist
            else:
                result = result + dict_trad[char]
    return result
