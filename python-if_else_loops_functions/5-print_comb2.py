#!/usr/bin/python3

number = ""

for i in range(0, 100):
    if i == 99:
        number += "{:02d}".format(i)
    else:
        number += "{:02d}, ".format(i)

print("{}".format(number))
