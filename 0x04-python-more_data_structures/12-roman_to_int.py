#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    rom_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }
    numb = [rom_dict[x] for x in roman_string]
    output = 0
    for d in range(len(numb)):
        output += numb[d]
        if numb[d - 1] < numb[d] and d != 0:
            output -= (numb[d - 1] + numb[d - 1])
    return output
