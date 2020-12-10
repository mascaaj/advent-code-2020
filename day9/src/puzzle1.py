""" Puzzle for dayX advent of code 2020
"""
from itertools import combinations
import numpy as np

if __name__ == "__main__":
    #Read file into numpy array
    filename = "../data/data.txt"
    data = np.genfromtxt(filename, delimiter=',')

    #intialization
    preamble_count=25
    result_array=[]
    flag=1
    #Prefill the arrary with zero using preamble length
    for arr in range(0,preamble_count):
        result_array.append(0)

    for i in enumerate(data):
        #Report data value if flag is zero
        if flag==0:
            flagged_num = i[0]-1+preamble_count
        result_array.append(flag)
        #Shift the preamble array
        preamble = data[i[0]:i[0]+preamble_count]
        #Test for bounds
        if (i[0]+preamble_count)<len(data):
            #Assign the test value
            test_val = data[i[0]+preamble_count]
            #This is the magic right here to find the combinations
            a = combinations(preamble,2)
            flag=0
            #iterate over combinations and sum
            for j in enumerate(list(a)):
                eval_sum = sum(j[1])
                if test_val == eval_sum:
                    flag=1
        else:
            break
    #Return output
    flagged_value = data[flagged_num]
    print("index : {}, value: {}".format(flagged_num,flagged_value))
