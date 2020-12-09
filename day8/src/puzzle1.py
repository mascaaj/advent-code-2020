""" Puzzle for dayX advent of code 2020
"""
import numpy as np
import pandas as pd

if __name__ == "__main__":
    # Read data into dataframe
    filename = '../data/data.txt'
    colnames = ["instr","val"]
    df = pd.read_csv(filename,names=colnames,header=None,sep= " ")
    # print(df)

    #Initialization
    instruction_log = []
    new_log = []
    row_check = 0
    acc_vec=[]
    acc=0

    #If the loop reaches the last row, break
    while row_check<=df.shape[0]:
        #Test for nop/acc/jmp, increment accumulator
        if df["instr"][row_check]=="nop":
            instruction_log.append(row_check)
            row_check+=1
    #         print("nop")

        if df["instr"][row_check]=="acc":
            instruction_log.append(row_check)
            acc = acc + df["val"][row_check]
            row_check+=1
    #         print("acc")


        if df["instr"][row_check]=="jmp":
            instruction_log.append(row_check)
            row_check = row_check + df["val"][row_check]
    #         print("jmp")
        #Test to see if unique values in the array of rows travelled == array
        #of rows travelled. If not, loop has started recursion
        acc_vec.append(acc)
        new_log = np.unique(instruction_log)
        new_log = new_log.tolist()

        #If recursion, break, print value to console
        if len(instruction_log)!=len(new_log):
            print("Found recursion")
            print("accumulator value:",acc_vec[-2])
            break
