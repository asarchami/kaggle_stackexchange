import pandas as pd
import os
from bs4 import BeautifulSoup


def _import_csv():
    # Here we concat multiple training csvs to a single one and
    # clean the results from html tags and stuff and save it to file
    if os.path.exists('dataset/all_csvs.csv'):
        return pd.read_csv(
            'dataset/all_csvs.csv', index_col=0, encoding='utf8')
    else:
        files = ['biology', 'cooking', 'crypto', 'diy', 'robotics', 'travel']
        filenames = ["dataset/{}.csv".format(filename) for
                     filename in files]
        csvs = []
        for filename in filenames:
            df = pd.read_csv(filename, encoding='utf-8')
            df['file_name'] = filename
            csvs.append(df)
        df = _clean_dataset(pd.concat(csvs, axis=0).reset_index())
        df.to_csv('dataset/all_csvs.csv', encoding='utf8')
        return df
    # returns the dataframe


def _clean_dataset(data):
    # cleans the dataframe from unwanted columns and html tags
    # also handles some unicode stuff
    if 'id' in data.columns:
        data = data.drop('id', axis=1)
    if 'index' in data.columns:
        data = data.drop('index', axis=1)
    data.content = data.content.apply(
        lambda x: BeautifulSoup(x, "lxml").text.replace('\n', ' '))
    data.file_name = data.file_name.str.replace(
        'dataset/', '').str.replace('.csv', '')
    # changes non-unicode columns to unicode
    for column in data.columns:
        if (
            data[column].dtype == 'object'
            ) and (
                type(data.loc[0, column]) != unicode):
            data[column] = data.loc[:, column].str.decode('utf-8')
    return data


def get_data():
    return _import_csv()
