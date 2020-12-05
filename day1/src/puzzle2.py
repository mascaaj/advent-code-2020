import numpy as np
import pandas as pd

# Read data in using pandas
df = pd.read_csv("../data/data.txt")
rows = df.shape[0]
value = 0

# begin counter and sorter.
for row in range(0,rows):
#     print(df.iloc[row,0])
    for row2 in range(0,rows):
#       print(df.iloc[row,0])
#       value = df.iloc[row,0] + df.iloc[row2,0]
        for row3 in range(0,rows):
        #       print(df.iloc[row,0])
                value = df.iloc[row,0] + df.iloc[row2,0] + df.iloc[row3,0]
                if value == 2020:
                    product = df.iloc[row,0] * df.iloc[row2,0] * df.iloc[row3,0]
                    # print all qualified numbers and products
                    print("element1: {}, element2: {}, element3 : {}, sum: {}, product: {}".format(df.iloc[row,0],df.iloc[row2,0],df.iloc[row3,0],value, product))
