""" Puzzle for dayX advent of code 2020
"""
import numpy as np
import pandas as pd

if __name__ == "__main__":
    # Read data into dataframe
    filename = '../data/data.txt'
    colnames = ["instr","val","jmp","nop"]
    df = pd.read_csv(filename,names=colnames,header=None,sep= " ")
    # print(df)

    #Initialization
    row_check = 0
    acc_vec=[]
    jmp_vec = []
    acc=0

    #If the loop reaches the last row, break
    while row_check<df.shape[0]:
        print("accumulator_value:",acc)
        print("flag")
        flag=0
        acc=0
        instruction_log = []
        new_log = []
        #flag in recursive loop, restarts the filter (might have redundant code)
        while flag == 0:
            #Test for nop/acc/jmp, increment accumulator
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
            #Test to see if unique values in the array of rows travelled == array
            #of rows travelled. If not, loop has started recursion
            acc_vec.append(acc)
            new_log = np.unique(instruction_log)
            new_log = new_log.tolist()
            #If recursion, break, capture the vector of jmp in the array found
            if len(instruction_log)!=len(new_log):
                flag=1
                print("recursion found")
                jmp_vec = []
                for row in range(len(new_log),0,-1):
                    index = instruction_log[row]
                    if df["instr"][index]=="jmp":
                        jmp_vec.append(index)
                # print(len(jmp_vec))
                break
        print(acc)
        break

    print(jmp_vec)

    # Read in dataframe on each loop, change one jmp value, test to reach end of file
    # Prolly not efficient, but should break when no more traversal thru dataframe is possible
    for i in enumerate(jmp_vec):
        colnames = ["instr","val","jmp","nop"]
        df_temp = pd.read_csv(filename,names=colnames,header=None,sep= " ")

        df_temp["instr"][i[1]]="nop"
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
                print("Recursion, Restarting with new value")
                break
