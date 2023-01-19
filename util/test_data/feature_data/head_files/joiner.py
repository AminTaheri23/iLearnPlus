# this python script will read the file and join across the lines
# and write the output to the file

import pandas as pd
import numpy as np
import os

def csv_reader_low(path):
    df_test = pd.read_csv(f'{path}', nrows=100)
    float_cols = [c for c in df_test if df_test[c].dtype == "float64"]
    float16_cols = {c: np.float16 for c in float_cols}
    float16_cols['SampleName'] = str
    float16_cols['label'] = bool
    df = pd.read_csv(f'{path}', engine='c', dtype=float16_cols)
    return df

# loop through all .csv files in the directory
# and join them together
# and write the output to the file
def join_files():
    df = csv_reader_low("ANF.csv")
    lens = len(df.columns)-2
    for file in os.listdir(os.getcwd()):
        # file =+ file
        # print(file)
        if file.endswith(".csv") and (not file.endswith("ANF.csv")):
            # read the file
            df1 = csv_reader_low(file, )

            # append the file name to the all column names except the first two columns
            df1.columns = df1.columns[:2].tolist() + [file.replace(".csv",'') + "_" + col for col in df1.columns[2:]]

            lens += len(df1.columns)-2
            # join the files
            col_name = file.replace(".csv",'')
            print(col_name)
            df = pd.merge(df, df1, how='outer', on=['SampleName', 'label'], )
    return df,lens

if __name__ == "__main__":
    df,lens = join_files()
    # write the output to the file
    print(df.head())
    print(df.columns[::50])
    print(lens + 2)
    print(len(df))
    df.to_csv("joined.csv", index=False)
