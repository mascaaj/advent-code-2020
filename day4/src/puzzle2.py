import pandas as pd
import numpy as np
import math
import re

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
        # print(x[0]=="\n")
        # print("Line {}: {}".format(lncnt, ln.strip()))
        # If not newline, enter the loop
        if (x[0]=="\n")==False:
            #Iterate till nextline
            counter=counter+1
            # print(counter)
            if counter!=0:
                # Split into bins.
                for i in range(0,len(x)):
                    b = x[i].split(":")
                    # print(b[0])
                    if b[0] == "byr":
                        # print("condition test",b[1],int(b[1])>=1920 and int(b[1])<=2002)
                        if int(b[1])>=1920 and int(b[1])<=2002:
                            byr_flag=byr_flag+1
                    elif b[0] == "iyr":
                        # print('condition test',b[1],int(b[1])>=2010 and int(b[1])<=2020)
                        if int(b[1])>=2010 and int(b[1])<=2020:
                            iyr_flag=iyr_flag+1
                    elif b[0] == "eyr":
                        # print('condition test',b[1],int(b[1])>=2020 and int(b[1])<=2030)
                        if int(b[1])>=2020 and int(b[1])<=2030:
                            eyr_flag=eyr_flag+1
                    elif b[0] == "hgt":
                        # print("condition1 test",b[1],bool(re.match(r"([0-9]+)([a-z]+)", b[1], re.I)))
                        # using regex expressions to split alpha numeric values
                        match = re.match(r"([0-9]+)([a-z]+)", b[1], re.I)
                        if match:
                            items = match.groups()
                            if items[1]=="in" and int(items[0])>=59 and int(items[0])<=76:
                                # print("condition2 test inches",items[0],int(items[0])>=59 and int(items[0])<=76)
                                hgt_flag=hgt_flag+1
                            elif items[1]=="cm" and int(items[0])>=150 and int(items[0])<=193:
                                # print("condition2 test cms",items[0],int(items[0])>=150 and int(items[0])<=193)
                                hgt_flag=hgt_flag+1
                                # print(items[0])
                    elif b[0] == "hcl":
                        # print("condition 1",b[1],bool(re.match(r"([#])([A-Fa-f0-9]+)", b[1], re.I)))
                        # using regex expressions to split alpha numeric values
                        match = re.match(r"([#])([A-Fa-f0-9]+)", b[1], re.I)
                        if match:
                            items = match.groups()
                            # print('condition2',items[1],len(items[1])==6)
                            if len(items[1])==6:
                                hcl_flag=hcl_flag+1
                    elif b[0] == "ecl":
                        match = re.match(r"([a-z]+)", b[1], re.I)
                        if match:
                            items = match.groups()
                            # print("condition 1",items,items[0] == "amb" or items[0] == "blu" or items[0] == "brn" or items[0] == "gry" or items[0] == "grn" or items[0] == "hzl" or items[0] == "oth")
                            if items[0] == "amb" or items[0] == "blu" or items[0] == "brn" or items[0] == "gry" or items[0] == "grn" or items[0] == "hzl" or items[0] == "oth":
                                ecl_flag=ecl_flag+1
                    elif b[0] == "pid":
                        match = re.match(r"([0-9]+)", b[1], re.I)
                        if match:
                            items = match.groups()
                            # print("condition1",items[0],len(items[0])==9,len(b[1])==9)
                            if len(items[0])==9:
                                pid_flag=pid_flag+1
                    elif b[0] == "cid":
                        cid_flag=cid_flag+1
        else:
            # When new line, calculate validity
            test = byr_flag*iyr_flag*eyr_flag*hgt_flag*hcl_flag*ecl_flag*pid_flag
            # print("test Value:",test)
            if test ==1:
                # print("valid")
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
            # print("valid counter:",validCounter)
            # print("total counter :", totalCounter)

        ln = fn.readline()
        lncnt += 1
    print("valid counter:",validCounter)
    print("total counter :", totalCounter)
