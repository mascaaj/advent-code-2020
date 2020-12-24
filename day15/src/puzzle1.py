""" Puzzle for day15 advent of code 2020
"""
import numpy as np
import pandas as pd
import math
import re

def find_key(input_dict, value):
    return {k for k, v in input_dict.items() if v == value}

def add_if_key_not_exist(dict_obj, value, iteration):
    """ Add new key-value pair to dictionary only if
    key does not exist in dictionary. """
    if len(list(find_key(dict_obj,value)))==1:
        # print("loop1")
        dict_obj.update({iteration: 0})
    else:
        # print("loop2")
        foundIndex = list(find_key(dict_obj,value))
        foundIndex.sort()
        # print(foundIndex)
        # print(newList)
        newVal = abs(foundIndex[-1] - foundIndex[-2])
        # print("foundIndex, iteration, value", foundIndex[-1], iteration, value, newVal)
        dict_obj.update({iteration: newVal})
    return dict_obj

def split_input(split_array):
    a = split_array.split(sep=",")
    map_object = map(int,a)
    int_vals = list(map_object)
    return int_vals

def solve(input_data):
    for i in enumerate(input_data):
        # print(i[2])
        split_vals = split_input(i[1])
        dictofvals = { j : split_vals[j] for j in range(0, len(split_vals) ) }
        # print("dictionary",dictofvals)
        for p in range(0,30000000):
            print(p)
            testval = dictofvals.get(p-1)
            # print(testval)
            if p>4:
                dictofvals = add_if_key_not_exist(dictofvals,testval,p)
                # print(dictofvals)
        # print(dictofvals)
        print(dictofvals.get(30000000))


if __name__ == "__main__":
    filename = "../data/data.txt"
    input_data = [i[:-1] for i in open(filename, "r").readlines()]
    result_filename = "../data/test_results2.txt"
    results = [i[:-1] for i in open(result_filename, "r").readlines()]
    # print(results)
    solve(input_data)
    # print(results)
