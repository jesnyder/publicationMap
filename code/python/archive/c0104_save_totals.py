import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def save_totals():
    """
    """
    metadata_path = os.path.join('metadata')
    metadata_file = os.path.join(metadata_path, 'publishedMetadata.csv')
    metadata_file = os.path.join(metadata_path, 'locations_defined.csv')
    df = pd.read_csv(metadata_file)

    col_names = df.head()
    for name in col_names:
        if 'Unnamed' in name:
            del df[name]

    df = df.dropna()

    df = df.drop_duplicates(subset=['titlePaper'])


    titles = list(df['titlePaper'])
    citations = list(df['citations'])

    df_summary = pd.DataFrame([])
    df_summary['counts'] = [len(titles)]
    df_summary['citations'] = [sum(citations)]

    summary_file = os.path.join(metadata_path, 'summary.csv')
    df_summary.to_csv(summary_file)
