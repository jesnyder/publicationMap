import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def save_totals(metadata_path):
    """
    """

    metadata_file = os.path.join(metadata_path, 'publishedMetadata.csv')
    df = pd.read_csv(metadata_file)

    col_names = df.head()
    for name in col_names:
        if 'Unnamed' in name:
            del df[name]

    df = df.dropna()

    summary_file = os.path.join(metadata_path, 'summary.csv')
