#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    num_a = len(argv) - 1

    if num_a == 0:
        print("0 arguments.")
    elif num_a == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(num_a))

    for d, j in enumerate(argv[1:]):
        print("{}: {}".format(d + 1, j))
