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
print(df.shape)

print(df.iloc[0,1])

#initialization
newcheck =0
count = -1
rowlength = 31*rows
col_offset = 1
row_offset = 2
flag = 0
newcheck=newcheck + col_offset + (row_offset*rowlength)

# Data Checker
for row in range(0,rows):
    a = df.iloc[row,1]
#     print(row)
    for l in a:
        count=count+1
#         print(l,count, newcheck)
        if newcheck == count:
            newcheck=newcheck + col_offset + (row_offset*rowlength)
            if l == '#':
                flag = flag +1
# Result
print(flag)
