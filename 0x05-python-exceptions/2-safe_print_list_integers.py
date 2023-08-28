#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    len_my_list = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            len_my_list += 1
        except (TypeError, ValueError):
            continue
    print()
    return len_my_list
