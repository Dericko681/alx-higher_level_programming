#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    mul_dict = a_dictionary.copy()
    my_keys = list(mul_dict.keys())

    for d in my_keys:
        mul_dict[d] *= 2

    return (mul_dict)
