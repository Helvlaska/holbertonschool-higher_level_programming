#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    True_False = []
    for i in my_list:
        if i % 2 == 0:
            True_False.append(True)
        else:
            True_False.append(False)
    return True_False
