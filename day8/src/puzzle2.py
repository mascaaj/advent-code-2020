""" Puzzle for dayX advent of code 2020
"""
import numpy as np
import pandas as pd

if __name__ == "__main__":

    filename = '../data/data.txt'
    colnames = ["instr","val","jmp","nop"]
    df = pd.read_csv(filename,names=colnames,header=None,sep= " ")
    # print(df)

    # instruction_log = []
    # new_log = []
    row_check = 0
    acc_vec=[]
    jmp_vec = []
    acc=0

    while row_check<df.shape[0]:
        print("accumulator_value:",acc)
        print("flag")
        flag=0
        acc=0
        instruction_log = []
        new_log = []
        while flag == 0:
            if df["instr"][row_check]=="nop":
                instruction_log.append(row_check)
                row_check+=1
    #             print("nop")

            if df["instr"][row_check]=="acc":
                instruction_log.append(row_check)
                acc = acc + df["val"][row_check]
                row_check+=1
    #             print("acc")

            if df["instr"][row_check]=="jmp":
                instruction_log.append(row_check)
    #             print("jmp")
                if df["val"][row_check]<0:
                    print("negative jump")
                row_check = row_check + df["val"][row_check]

            acc_vec.append(acc)
            new_log = np.unique(instruction_log)
            new_log = new_log.tolist()
            if len(instruction_log)!=len(new_log):
                flag=1
                print("here")
                jmp_vec = []
                for row in range(len(new_log),0,-1):
                    index = instruction_log[row]
                    if df["instr"][index]=="jmp":
                        jmp_vec.append(index)
                print(len(jmp_vec))
                break
        print(acc)
        break

    print(jmp_vec)

    print(jmp_vec)

    for i in range(0, len(jmp_vec)):
        colnames = ["instr","val","jmp","nop"]
        df_temp = pd.read_csv(filename,names=colnames,header=None,sep= " ")
        df_temp["instr"][jmp_vec[i]]="nop"
        print("accumulator_value:",acc)
        flag=0
        acc=0
        row_check = 0
        instruction_log = []
        new_log = []
        while flag == 0:
            if df_temp["instr"][row_check]=="nop":
                instruction_log.append(row_check)
                row_check+=1
            print(acc)
            if df_temp["instr"][row_check]=="acc":
                instruction_log.append(row_check)
                acc = acc + df_temp["val"][row_check]
                row_check+=1
            print(acc)
            if df_temp["instr"][row_check]=="jmp":
                instruction_log.append(row_check)
                row_check = row_check + df_temp["val"][row_check]
            print(acc)
            acc_vec.append(acc)
            new_log = np.unique(instruction_log)
            new_log = new_log.tolist()

            if len(instruction_log)!=len(new_log):
                flag=1
                print("here")
                break
