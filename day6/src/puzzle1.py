""" Puzzle for day6 advent of code 2020
"""

filename = '../data/data.txt'
import numpy as np

# Define functions
def histogram(word):
    """ Function to calculate histogram of letters in word
    """
    if not isinstance(word,str):
        raise TypeError("Please provide a string")
    dictionary = dict()
    for alphabet in word:
        if alphabet not in dictionary:
            dictionary[alphabet] = 1
        else:
            dictionary[alphabet] += 1
    return dictionary

with open(filename) as fn:
    #Read in the file line by line
    ln = fn.readline()
    #Initialization of variables
    [lncnt,counter,groupcounter]=[0,0,0]
    [total,ocount]=[0,0]
    catword=""
    while ln:
        #Check if not new line
#         print("Line {}: {}".format(lncnt, ln.strip()))
        if not ln=="\n":
            #Count up lines, concatenate to single word, remove newline
            counter+=1
            ln=ln.strip("\n")
#             print(counter)
            catword = catword + ln
        else:
#             print(counter)
#             print(catword)
            h=histogram(catword)
#             print(h)
            ocount = len(h)
#             print(ocount)
            groupcounter+=1
            [counter,catword]=[0,""]
            total = total + ocount
        ln = fn.readline()
        lncnt+=1
    #Print result
    print("total groups:",groupcounter)
    print("total:", total)
