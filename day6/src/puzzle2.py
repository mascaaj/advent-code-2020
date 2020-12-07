""" Puzzle for day6 advent of code 2020
"""
import numpy as np



# Define functions
def histogram(word):
    """ Function to calculate histogram of letters in word
    """
    dictionary = dict()
    for alphabet in word:
        if alphabet not in dictionary:
            dictionary[alphabet] = 1
        else:
            dictionary[alphabet] += 1
    return dictionary

def hist_val_check(hist,val,normalizer):
    """ Function to ingest histogram,
        Normalize based on max occurances
        Find number of certain value in normalized array
    """
    histcount = np.fromiter(hist.values(),dtype="int")
    normalize = histcount/normalizer
    occurance_count = np.count_nonzero(normalize == val)
    return occurance_count


def test_hist_val_check():
    hist = histogram("macuziywlbapodgevujnskptruz")
    assert hist_val_check(hist,1,3) == 1

if __name__ == "__main__":
    filename = '../data/data.txt'
    with open(filename) as fn:
        #Read in the file line by line
        ln = fn.readline()
        #Initialization of variables
        [lncnt,counter,groupcounter]=[0,0,0]
        [total,ocount]=[0,0]
        catword=""
        while ln:
            #Check if not new line
            if not ln=="\n":
                #Count up lines, concatenate to single word, remove newline
                counter+=1
                ln=ln.strip("\n")
                catword = catword + ln
            else:
                #Check for frequency, normalize on count, check for occurance of 1
                h=histogram(catword)
                ocount = hist_val_check(h,1,counter)
                groupcounter+=1
                [counter,catword]=[0,""]
                total = total + ocount
            ln = fn.readline()
            lncnt+=1
        #Print result
        print("total groups:",groupcounter)
        print("total:", total)
