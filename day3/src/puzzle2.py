""" Puzzle for day3 advent of code 2020
"""
import pandas as pd

# Read in data using pandas
colnames=['data']
df = pd.read_csv("../data/data.txt",names=colnames,header=None)
# get shape of the df
rows = df.shape[0]

#Repeat the data row times
df['data_cat']=df['data']*rows

#initialization
rowlength = 31*rows
col_offset = [1,3,5,7,1]
row_offset = [1,1,1,1,2]
prod_flag = 1

# Data Checker
for i in range(0,len(col_offset)) :
    newcheck=0
    flag=0
    count=-1
    newcheck=newcheck + col_offset[i] + (row_offset[i]*rowlength)
    for row in range(0,rows):
        a = df.iloc[row,1]
    #     print(row)
        for l in a:
            count=count+1
    #         print(l,count, newcheck)
            if newcheck == count:
                newcheck=newcheck + col_offset[i] + (row_offset[i]*rowlength)
                if l == '#':
                    flag = flag +1

    print(flag)
    prod_flag = prod_flag*flag

# Result
print(prod_flag)
