""" Puzzle for dayX advent of code 2020
"""
import numpy as np
import pandas as pd

if __name__ == "__main__":

    filename = '../data/data.txt'
    colnames = ["instr","val"]
    df = pd.read_csv(filename,names=colnames,header=None,sep= " ")
    # print(df)

    instruction_log = []
    new_log = []
    row_check = 0
    acc_vec=[]
    acc=0
    while row_check<=df.shape[0]:

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

        acc_vec.append(acc)
        new_log = np.unique(instruction_log)
        new_log = new_log.tolist()
    #     print(row_check)
    #     print(instruction_log)
    #     print(new_log)
    #     print(acc_vec)
        if len(instruction_log)!=len(new_log):
            print("Found recursion")
            print("accumulator value:",acc_vec[-2])
            break
