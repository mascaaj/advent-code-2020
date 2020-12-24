# """ Puzzle for day18 advent of code 2020
# """
import numpy as np
import pandas as pd
import math
import re


def solve(input_data):
    print(input_data)
    # for i in enumerate(input_data):
        # print(i[2])
        # split_vals = split_input(i[1])
        # dictofvals = { j : split_vals[j] for j in range(0, len(split_vals) ) }
        # print("dictionary",dictofvals)
        # for p in range(0,30000000):
            # print(p)
            # testval = dictofvals.get(p-1)
            # print(testval)
            # if p>4:
                # dictofvals = add_if_key_not_exist(dictofvals,testval,p)
                # print(dictofvals)
        # print(dictofvals)
        # print(dictofvals.get(30000000))

if __name__ == "__main__":
    filename = "../data/test_data.txt"
    input_data = [i[:-1] for i in open(filename, "r").readlines()]
    result_filename = "../data/test_results2.txt"
    results = [i[:-1] for i in open(result_filename, "r").readlines()]
    # print(results)
    solve(input_data)
    # print(results)