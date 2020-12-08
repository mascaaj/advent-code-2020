""" Puzzle for dayX advent of code 2020
"""
import numpy as np
import pandas as pd
import math
import re


if __name__ == "__main__":
    filename = "../data/data.txt"
    df = pd.read_csv(filename, sep="\n", header=None)
    df = df[0].str.split(',',expand=True)
    df.columns = ["original", "content2", "content3", "content4"]

    df[["original","content1"]] = df['original'].str.split("contain",expand=True)
    # print(df)
    cols = df.shape[1]
    rows = df.shape[0]
    df["original_num"]=""
    df["original_color"]=""
    df["content1_num"]=""
    df["content1_color"]=""
    df["content2_num"]=""
    df["content2_color"]=""
    df["content3_num"]=""
    df["content3_color"]=""
    df["content4_num"]=""
    df["content4_color"]=""
    # print(df.head())

    def split_string_col(df,col_name,row):
        a = df[col_name][row]
        a2 = isinstance(a, float)
        if a2==False and a is not None:
            b = a
            c = b.split(" ")
            if not c[0]=="no" :
                df[col_name+"_color"][row] = c[2]+c[3]
                df[col_name+"_num"][row] = c[1]
            else:
                df[col_name+"_color"][row] = "no"
                df[col_name+"_num"][row] = 0
        else:
            df[col_name][row] = "no"
            df[col_name+"_color"][row] = "no"
            df[col_name+"_num"][row] = 0
        return(df)

    def split_string_col2(df,col_name,row):
        a = df[col_name][row]
        a2 = isinstance(a, float)
        if a2==False and a is not None:
            b = a
            c = b.split(" ")
            if not c[0]=="no" :
                df[col_name+"_color"][row] = c[0]+c[1]
                df[col_name+"_num"][row] = c[1]
            else:
                df[col_name+"_color"][row] = "no"
                df[col_name+"_num"][row] = 0
        else:
            df[col_name][row] = "no"
            df[col_name+"_color"][row] = "no"
            df[col_name+"_num"][row] = 0
        return(df)

    for i in range(1,cols):
        for row in range(0,rows):
            col_name="content"+str(i)
            df_c1 = split_string_col(df,col_name,row)

    for row in range(0,rows):
        col_name="original"
        df_final = split_string_col2(df,col_name,row)
    print(df_final)

    rows2 = df_final.shape[0]
    vals = ["shinygold"]
    test_vals = []
    for row in range(0,rows2):
        for i in range(0,len(vals)):
            if df_final["original_color"][row] == vals[0]:
                test_vals.append(df_final["original_color"][row])
                if not df_final["content1_color"][row]=="no":
                    test_vals.append(df_final["content1_color"][row])
                elif not df_final["content2_color"][row]=="no":
                    test_vals.append(df_final["content2_color"][row])
                elif not df_final["content3_color"][row]=="no":
                    test_vals.append(df_final["content3_color"][row])
                elif not df_final["content4_color"][row]=="no":
                    test_vals.append(df_final["content4_color"][row])
    test_vals = np.unique(test_vals)
    test_vals = test_vals.tolist()
    new_total = len(test_vals)
    print(new_total)


    old_total = 0
    new_total = 1
    while old_total !=new_total:
        old_total =  new_total
        for row in range(0,rows2):
            for i in range(0,len(test_vals)):
                if df_final["original_color"][row] == test_vals[i]:
                    test_vals.append(df_final["original_color"][row])
                    if not df_final["content1_color"][row]=="otherbags."and not df_final["content1_color"][row]=="otherbags.":
                        test_vals.append(df_final["content1_color"][row])
                        if not df_final["content2_color"][row]=="otherbags." and not df_final["content2_color"][row]=="no":
                            test_vals.append(df_final["content2_color"][row])
                            if not df_final["content3_color"][row]=="otherbags." and not df_final["content3_color"][row]=="no":
                                test_vals.append(df_final["content3_color"][row])
                                if not df_final["content4_color"][row]=="otherbags." and not df_final["content4_color"][row]=="no":
                                    test_vals.append(df_final["content4_color"][row])

        test_vals = np.unique(test_vals)
        test_vals = test_vals.tolist()
        new_total = len(test_vals)
        print(test_vals)
        print(new_total)


    for row in range(0,rows2):
        for i in range(0,len(test_vals)):
            if df_final["original_color"][row] == test_vals[i]:
                print(df.iloc[row,:])
