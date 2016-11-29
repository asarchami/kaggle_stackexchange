import glob as glob
import os
import pandas as pd
from bs4 import BeautifulSoup


def import_csv(targetdir):
    path = r'%s' % targetdir  # use your path
    allFiles = glob.glob(path + "/*.csv")
    frame = pd.DataFrame()
    list_ = []
    for file_ in allFiles:
        df = pd.read_csv(file_, index_col=None, header=0)
        df['file_name'] = file_
        list_.append(df)
    frame = pd.concat(list_)
    return frame


def clean_dataset(data):
    data.drop('id', axis=1)
    data.content = data.content.apply(
        lambda x: BeautifulSoup(x, "lxml").text.replace('\n', ' '))
    data.file_name = data.file_name.str.replace(
        'dataset/', '').str.replace('.csv', '')
    return data


def get_data(targetdir):
    return clean_dataset(import_csv(targetdir))
