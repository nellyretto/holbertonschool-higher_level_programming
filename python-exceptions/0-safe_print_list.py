#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    printed = 0
    try:
        for num in range(x):
            print(my_list[num], end="")
            printed += 1
    except IndexError:
        print()
    return printed
