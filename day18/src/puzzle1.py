# """ Puzzle for day18 advent of code 2020
# """
import numpy as np
import pandas as pd
import math
import re

def num_groups(regex):
    return len(re.compile(regex).groups)

def action_operator(s1,s2,op):
    

def recursive_bracket_parser(s, i):
    count=0
    while count < len(s):
        if s[count] == '(':
            # print("v1")
            i = i+1
        elif s[count] == ')':
            # print("v2")
            i = i+1
        else:
            pass
            # print("v3")
        count+=1
    return i

def solve(input_data):

    for exp in range(0,len(input_data)):
        # print(input_data[exp])
        s = input_data[exp]
        print(recursive_bracket_parser(s,0))

        # if re.search(r'\((.*?)\)',s)!=None:
        #     print("brackets")
        #     paren =  re.search(r'\((.*?)\)',s)
        #     a = paren.groups(1)
        #     print(a)
        #     len_groups = len(paren.groups())
        #     if re.search(r'\((.*?)\)',a)!=None:
        #         print("here")
        #         # paren2 =  re.search(r'\((.*?)\)',paren.group(1))
        #         # len_groups = len(paren2.groups())
        #     else:
        #         pass

        # else:
        #     print("no brackets")
    


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
    filename = "../data/data.txt"
    input_data = [i[:-1] for i in open(filename, "r").readlines()]
    result_filename = "../data/test_results.txt"
    results = [i[:-1] for i in open(result_filename, "r").readlines()]
    # print(results)
    solve(input_data)
    # print(results)