#!/usr/bin/python3

def read_file(filename=""):
    with open(f"{filename}", "r") as f:
        content = f.read()
    print(content)
