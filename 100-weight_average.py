#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return (0)
    score_sum = 0
    weight_sum = 0
    for tup in my_list:
        score_sum += (tup[0] * tup[1])
        weight_sum += tup[1]
    average = score_sum / weight_sum
    return average
