""" Puzzle for dayX advent of code 2020
"""
import numpy as np
import pandas as pd

def split_string_col(df1,col_name1,row1):
    """Function to parse and split the names of the bags
    """
    val = df1[col_name1][row1]
    val2 = isinstance(val, float)
    if not val2 and val is not None:
        sp_val = val.split(" ")
        if not sp_val[0]=="no" :
            df1[col_name1+"_color"][row1] = sp_val[2]+sp_val[3]
            df1[col_name1+"_num"][row1] = sp_val[1]
        else:
            df1[col_name1+"_color"][row1] = "no"
            df1[col_name1+"_num"][row1] = "no"
    else:
        df1[col_name1][row] = "no"
        df1[col_name1+"_color"][row1] = "no"
        df1[col_name1+"_num"][row1] = "no"
    return df1

def split_string_col2(df2,col_name2,row2):
    """Function to parse and split the names of the bags
    """
    val = df2[col_name2][row2]
    val2 = isinstance(val, float)
    if not val2 and val is not None:
        sp_val = val.split(" ")
        if not sp_val[0]=="no" :
            df2[col_name2+"_color"][row2] = sp_val[0]+sp_val[1]
            df2[col_name2+"_num"][row2] = sp_val[1]
        else:
            df2[col_name2+"_color"][row2] = "no"
            df2[col_name2+"_num"][row2] = "no"
    else:
        df2[col_name2][row2] = "no"
        df2[col_name2+"_color"][row2] = "no"
        df2[col_name2+"_num"][row2] = "no"
    return df2


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

    for i in range(1,cols):
        for row in range(0,rows):
            col_name="content"+str(i)
            df_c1 = split_string_col(df,col_name,row)

    for row in range(0,rows):
        col_name="original"
        df_final = split_string_col2(df,col_name,row)
    # print(df)

    rows2 = df_final.shape[0]
    vals = ["shinygold"]
    test_vals = []
    for row in range(0,rows2):
        if df_final["content1_color"][row] == vals[0]:
            df_final["original_num"][row] = 1
            test_vals.append(df_final["original_color"][row])
        elif df_final["content2_color"][row] == vals[0]:
            df_final["original_num"][row] = 1
            test_vals.append(df_final["original_color"][row])
        elif df_final["content3_color"][row] == vals[0]:
            df_final["original_num"][row] = 1
            test_vals.append(df_final["original_color"][row])
        elif df_final["content4_color"][row] == vals[0]:
            df_final["original_num"][row] = 1
            test_vals.append(df_final["original_color"][row])
        else:
            df_final["original_num"][row] = 0


    test_vals = np.unique(test_vals)
    test_vals = test_vals.tolist()
    # print(test_vals)
    # print(len(test_vals))
    old_total = 0
    new_total = 1
    while old_total!=new_total:
        old_total =  new_total
        for row in range(0,rows2):
            for i in enumerate(test_vals):
                if df_final["content1_color"][row] == i[1]:
                    df_final["original_num"][row] = 1
                    test_vals.append(df_final["original_color"][row])
                elif df_final["content2_color"][row] == i[1]:
                    df_final["original_num"][row] = 1
                    test_vals.append(df_final["original_color"][row])
                elif df_final["content3_color"][row] == i[1]:
                    df_final["original_num"][row] = 1
                    test_vals.append(df_final["original_color"][row])
                elif df_final["content4_color"][row] == i[1]:
                    df_final["original_num"][row] = 1
                    test_vals.append(df_final["original_color"][row])
        test_vals = np.unique(test_vals)
        test_vals = test_vals.tolist()
        print(test_vals)
        new_total = len(test_vals)
        print(new_total)


    for row in range(0,rows2):
        for i in enumerate(test_vals):
            if df_final["original_color"][row] == i[1]:
                df_final["original_num"][row] = 1


    print(df_final["original_num"])
    print(sum(df_final["original_num"]))
