from PIL import Image
import glob

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def aggregate_information():
    """
    This performs no function.
    Intended to automate creation on an aggregated file for building map
    """

    print("running aggregate_information")

    pub_path = os.path.join('searchResults', 'pubs', 'manuallyCollected')
    if not os.path.isdir(pub_path): os.mkdir(pub_path)
    pub_file = os.path.join(pub_path, 'publicationMetadata'  + '.csv')
    df = pd.read_csv(pub_file)

    del df['Unnamed: 0']

    pub_path = os.path.join('metadata')
    if not os.path.isdir(pub_path): os.mkdir(pub_path)
    pub_file = os.path.join(pub_path, 'publishedMetadata'  + '.csv')
    df.to_csv(pub_file)


    print('completed aggregate_information')
