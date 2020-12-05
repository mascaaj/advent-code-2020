# Puzzle 2 for advent of code 2020
import numpy as np
import pandas as pd
import math
import re

#Read file using pandas, assign rowlength
path = "../data/data.txt"
colnames = ['data','row','seat','seat_id']
df = pd.read_csv(path, names=colnames, header=None)
datRows = df.shape[0]

for row in range(0, datRows):
    #initialization
    max_lim = 127
    min_lim = 0
    max_seat = 7
    min_seat = 0
    seatCode = df.iloc[row,0]
#     print(seatCode)
#     print("count:{},min_lim: {},max_lim: {}".format(seatCode[0],min_lim, max_lim))
#     Find the seat number
    for i in seatCode[0:6]:
        interval = round((max_lim-min_lim)/2,0)
        if i == 'F':
            min_lim=min_lim
            max_lim=max_lim-interval
        else:
            max_lim=max_lim
            min_lim=min_lim+interval
#             print("count:{},min_lim: {},max_lim: {}".format(i,min_lim, max_lim))
#   Final Arbitration for row number
    if seatCode[6]=="F":
        df.iloc[row,1]=min_lim
    else:
        df.iloc[row,1]=max_lim
    # Begin Seat Arbitration
    for j in seatCode[7:len(seatCode)-1]:
#         print(j)
        seat_interval = round((max_seat-min_seat)/2,0)
        if j == 'L':
            min_seat=min_seat
            max_seat=max_seat-seat_interval
        else:
            max_seat=max_seat
            min_seat=min_seat+seat_interval
#         print("count:{},min_lim: {},max_lim: {}".format(j,min_seat, max_seat))
    if seatCode[9]=="L":
        df.iloc[row,2]=min_seat
    else:
        df.iloc[row,2]=max_seat
    df.iloc[row,3]=df.iloc[row,1]*8 +df.iloc[row,2]
# print(max(df["seat_id"]))

# create plane map
df_plane =  pd.DataFrame(np.zeros((128,8)))
for row in range(0,datRows):
    r = int(df.iloc[row,1])
    c = int(df.iloc[row,2])
#     print(r,c)
    df_plane.iloc[r,c]=1.0

#Find all rows that have values == 0
plane_map=df_plane[(df_plane.values.ravel() == 0.0).reshape(df_plane.shape).any(1)]
print(plane_map)
print("seats cannot be towards the forward or end of the plane")
print("seats have non empty values before on all directions (except edges)")
