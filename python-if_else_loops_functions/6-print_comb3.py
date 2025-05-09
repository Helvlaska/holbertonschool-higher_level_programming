#!/usr/bin/python3

number = ""

for i in range(0, 10):
    for j in range(0, 10):
        if i < j:
            number += "{}{}, ".format(i, j)

print("{}".format(number.strip(", ")))
