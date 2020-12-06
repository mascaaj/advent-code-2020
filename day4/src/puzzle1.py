""" Puzzle for day4 advent of code 2020
"""
# import math
# import pandas as pd
# import numpy as np


#solving this with string processing.
filename = '../data/data.txt'
with open(filename) as fn:
    # Read each line
    ln = fn.readline()
    #intialize Counters / Flags
    lncnt = 0
    validCounter=0
    totalCounter=0
    counter=0
    byr_flag = 0
    iyr_flag = 0
    eyr_flag = 0
    hgt_flag = 0
    hcl_flag = 0
    ecl_flag = 0
    pid_flag = 0
    cid_flag = 0

    while ln:
        # Begin spliting the first line with space delim.
        x = ln.split(" ")
        # Print line value.
        print("Line {}: {}".format(lncnt, ln.strip()))
        # If not newline, enter the loop
        if not x[0]=="\n":
            #Iterate till nextline
            counter=counter+1
            if counter!=0:
                #Split into bins.
                for i in enumerate(x):
                    b = x[i[0]].split(":")
                    if b[0] == "byr":
                        byr_flag=byr_flag+1
                    elif b[0] == "iyr":
                        iyr_flag=iyr_flag+1
                    elif b[0] == "eyr":
                        eyr_flag=eyr_flag+1
                    elif b[0] == "hgt":
                        hgt_flag=hgt_flag+1
                    elif b[0] == "hcl":
                        hcl_flag=hcl_flag+1
                    elif b[0] == "ecl":
                        ecl_flag=ecl_flag+1
                    elif b[0] == "pid":
                        pid_flag=pid_flag+1
                    elif b[0] == "cid":
                        cid_flag=cid_flag+1
        else:
            #When new line, calculate validity
            test = byr_flag*iyr_flag*eyr_flag*hgt_flag*hcl_flag*ecl_flag*pid_flag
            print("test Value:",test)
            if test ==1:
                print("valid")
                validCounter= validCounter+1
            totalCounter = totalCounter +1
            #reset flags
            byr_flag = 0
            iyr_flag = 0
            eyr_flag = 0
            hgt_flag = 0
            hcl_flag = 0
            ecl_flag = 0
            pid_flag = 0
            cid_flag = 0
            print("valid counter:",validCounter)
            print("total counter :", totalCounter)

        ln = fn.readline()
        lncnt += 1
    print("valid counter:",validCounter)
    print("total counter :", totalCounter)
