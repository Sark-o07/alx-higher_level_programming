#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list == []:
        return [None]
    else:
        list_result = []
        for num in my_list:
            if num % 2 == 0:
                list_result.append(True)
            else:
                list_result.append(False)
        return list_result
