import pandas as pd
import os


def read_files():
    filenames = ["dataset/"+filename for filename in os.listdir("dataset") if filename.endswith(".csv")]
    return pd.concat([pd.read_csv(filename) for filename in filenames], axis=0).reset_index()
