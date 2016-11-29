import pandas as pd
import os
from bs4 import BeautifulSoup


def import_csv():
    filenames = ["dataset/"+filename for filename in os.listdir("dataset") if filename.endswith(".csv")]
    csvs = []
    for filename in filenames:
        df = pd.read_csv(filename)
        df['file_name'] = filename
        csvs.append(df)
    return pd.concat(csvs, axis=0).reset_index()

def clean_dataset(data):
    data = data.drop(['id', 'index'], axis=1)
    data.content = data.content.apply(
        lambda x: BeautifulSoup(x, "lxml").text.replace('\n', ' '))
    data.file_name = data.file_name.str.replace(
        'dataset/', '').str.replace('.csv', '')
    return data


def get_data():
    return clean_dataset(import_csv())
