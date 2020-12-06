""" Puzzle for day2 advent of code 2020
"""
import pandas as pd


#Read in data using pandas
colnames=['min_limits', 'constraint', 'pwd']
df = pd.read_csv("../data/data.txt",sep=" ",names=colnames, header=None)

#Clean df, split strings
df[['min_limits','max_lim']] = df['min_limits'].str.split('-',expand=True)
df[['constraint','count']] = df['constraint'].str.split(':',expand=True)
count =0
rows = df.shape[0]

#Begin count for condition
for row in range(0,rows):
#     print(df.iloc[row,2])
    count=0
    for x in df.iloc[row,2]:
        if x==df.iloc[row,1]:
            count=count +1
#     print(count)
    df.iloc[row,4]= count
print(df)

#Convert the split columns into numeric
df['min_limits'] = pd.to_numeric(df['min_limits'])
df['max_lim'] = pd.to_numeric(df['max_lim'])
df['count'] = pd.to_numeric(df['count'])
counter=0

#Final counter for validity
for row in range(0,rows):
    if df.iloc[row,4]<=df.iloc[row,3] and df.iloc[row,4]>=df.iloc[row,0]:
        counter=counter+1
    else:
        pass

#Result
print(counter)
