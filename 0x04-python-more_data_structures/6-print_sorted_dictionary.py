#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    my_order = list(a_dictionary.keys())
    my_order.sort()

    for d in my_order:
        print("{}: {}".format(d, a_dictionary.get(d)))
