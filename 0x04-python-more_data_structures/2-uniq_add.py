#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = list(set(my_list))
    sum_ = 0
    for element in uniq_list:
        sum_ += element
    return sum_
