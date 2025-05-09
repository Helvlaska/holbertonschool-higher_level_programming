#!/usr/bin/python3

hexa = ""

for i in range(0, 99):
    hexa += "{} = {}\n".format(i, hex(i))

print("{}".format(hexa), end="")
