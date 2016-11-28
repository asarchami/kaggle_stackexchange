import pandas as pd
import re
import glob

def import_csv():
    path =r'dataset' # use your path
    allFiles = glob.glob(path + "/*.csv")
    frame = pd.DataFrame()
    list_ = []
    for file_ in allFiles:
        df = pd.read_csv(file_,index_col=None, header=0)
        list_.append(df)
    return pd.concat(list_)

csv = import_csv()
print csv
