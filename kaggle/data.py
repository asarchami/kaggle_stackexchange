import pandas as pd
import os
from bs4 import BeautifulSoup


def import_csv():
    filenames = ["dataset/"+filename for filename in os.listdir("dataset") if filename.endswith(".csv")]
    csvs = []
    for filename in filenames:
        df = pd.read_csv(filename, encoding = 'utf-8')
        df['file_name'] = filename
        csvs.append(df)
    return pd.concat(csvs, axis=0).reset_index()

def clean_dataset(data):
    data = data.drop(['id', 'index'], axis=1)
    data.content = data.content.apply(
        lambda x: BeautifulSoup(x, "lxml").text.replace('\n', ' '))
    data.file_name = data.file_name.str.replace(
        'dataset/', '').str.replace('.csv', '')
    # changes non-unicode columns to unicode
    for column in data.columns:
        if (data[column].dtype == 'object') and (type(data.loc[0, column]) != unicode):
            data[column] = data.loc[:,column].str.decode('utf-8')
    return data


def get_data():
    return clean_dataset(import_csv())
