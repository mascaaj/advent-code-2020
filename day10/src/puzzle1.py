""" Puzzle for day10 advent of code 2020
"""
import numpy as np

if __name__ == "__main__":
    # Readin file
    filename = "../data/data.txt"
    data = np.genfromtxt(filename, delimiter=',')
    print(data)
    #Initialization
    result_array=[0]
    diff_array = []
    last_val=0
    # Sort the data to improve the search
    data = np.sort(data)
    # Iterate and check add sum and results array
    while len(result_array) < len(data):
        print(len(result_array))
        for i in enumerate(data):
            diff = i[1] - last_val
            if diff == 1:
                last_val = i[1]
                result_array.append(last_val)
                diff_array.append(diff)
            else:
                if diff == 2:
                    last_val = i[1]
                    result_array.append(last_val)
                    diff_array.append(diff)
                else:
                    if diff == 3:
                        last_val = i[1]
                        result_array.append(last_val)
                        diff_array.append(diff)

    #Process output to get desired output.
    print(result_array)
    print(diff_array)
    b,c = np.unique(diff_array,return_counts=True)
    print("1 counts:", c[0])
    print("3 counts:", c[1]+1)
    product = c[0] * (c[1]+1)
    print(product)
