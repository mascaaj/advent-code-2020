""" Puzzle for day5 advent of code 2020
"""

# Puzzle 1 for advent of code 2020
import pandas as pd


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
            max_lim=max_lim-interval
        else:
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
            # min_seat=min_seat
            max_seat=max_seat-seat_interval
        else:
            # max_seat=max_seat
            min_seat=min_seat+seat_interval
#         print("count:{},min_lim: {},max_lim: {}".format(j,min_seat, max_seat))
    if seatCode[9]=="L":
        df.iloc[row,2]=min_seat
    else:
        df.iloc[row,2]=max_seat
    df.iloc[row,3]=df.iloc[row,1]*8 +df.iloc[row,2]
print(max(df["seat_id"]))
