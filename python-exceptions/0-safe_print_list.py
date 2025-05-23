#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for _ in range(x):
        try:
            print(my_list[count], end="")
            count = count + 1
        except IndexError:
            break
    print()
    return count
