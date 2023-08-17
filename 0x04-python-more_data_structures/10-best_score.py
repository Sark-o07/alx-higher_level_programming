#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    else:
        highest_score = 0
        for v in a_dictionary.values():
            if highest_score < v:
                highest_score = v
        for k, v in a_dictionary.items():
            if v == highest_score:
                return k

