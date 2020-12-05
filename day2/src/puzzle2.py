import pandas as pd
import numpy as np

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
print(df.head(10))
#Convert the split columns into numeric
df['min_limits'] = pd.to_numeric(df['min_limits'])
df['max_lim'] = pd.to_numeric(df['max_lim'])
df['count'] = pd.to_numeric(df['count'])

#Final counter for positional validity
counter2=0
for row in range(0,rows):
# for row in range(0,10):
#     print(df.iloc[row,2])
    counter1=0
    flag=0
    for x in df.iloc[row,2]:
#         print("x1",x)
        counter1 = counter1 +1
#         print(counter1)
        if x==df.iloc[row,1]:
            if counter1==df.iloc[row,0]:
                flag=flag+1
            elif counter1==df.iloc[row,3]:
                flag=flag+1
            else:
                pass
#         print(flag)
    if flag==1:
        counter2=counter2+1

#Result
print(counter2)
