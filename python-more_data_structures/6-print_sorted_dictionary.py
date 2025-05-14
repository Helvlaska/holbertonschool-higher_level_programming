#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for order_key in sorted(a_dictionary):
        print(f"{order_key}: {a_dictionary[order_key]}")
