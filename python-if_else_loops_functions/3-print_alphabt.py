#!/usr/bin/python3

alphabet = ""

for i in range(97, 123):
    if i == 101 or i == 113:
        continue
    else:
        alphabet += chr(i)

print("{}".format(alphabet), end="")