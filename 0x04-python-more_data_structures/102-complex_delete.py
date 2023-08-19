#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_list = a_dictionary.copy()
    for k, v in new_list.items():
        if v == value:
            del k
    return new_list
