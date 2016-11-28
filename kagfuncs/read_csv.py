import glob as glob
import os
import pandas as pd

def import_csv(targetdir):
    path =r'%s' % targetdir # use your path
    allFiles = glob.glob(path + "/*.csv")
    frame = pd.DataFrame()
    list_ = []
    for file_ in allFiles:
        df = pd.read_csv(file_,index_col=None, header=0)
        df['file_name'] = file_
        list_.append(df)
    frame = pd.concat(list_)
    return frame
