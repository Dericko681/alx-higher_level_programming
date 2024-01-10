#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score = 0
    weight = 0
    for d in my_list:
        weight += d[0] * d[1]
        score += d[1]
        weighted_average = weight / score
    return weighted_average
