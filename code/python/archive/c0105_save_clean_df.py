import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def save_clean_df():
    """
    """
    metadata_path = os.path.join('metadata')
    metadata_file = os.path.join(metadata_path, 'metadata_editted.csv')
    df = pd.read_csv(metadata_file)

    col_names = df.head()
    for name in col_names:
        print('name = ' + name)
        if 'Unnamed' in name:
            del df[name]

    df = df.dropna()

    # del df['gpsLat, gpsLong']
    del df['publishedYear']
    del df['publishedMonth']
    del df['titlePaper']
    # del df['count']

    print('df = ')
    print(df)

    """
    df = df.drop_duplicates(subset=['count'])

    counts = list(df['count'])
    citations = list(df['citations'])

    df_summary = pd.DataFrame([])
    df_summary['counts'] = [len(counts)]
    df_summary['citations'] = [sum(citations)]
    """

    summary_file = os.path.join(metadata_path, 'table.csv')
    df.to_csv(summary_file)
