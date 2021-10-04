
from bs4 import BeautifulSoup

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pypatent
import requests

def search_clinic():
    """

    """

    print("running search_clinic")

    url = 'https://clinicaltrials.gov/ct2/search/advanced'
    search_terms = ['mesenchymal', 'exosome']

    df = pd.DataFrame()
    for term in search_terms:
        print('search ' + term + ' in ' + str(url) )

        clinic_path = os.path.join('searchResults', 'clinical')
        clinic_file = os.path.join(clinic_path, term + '.csv')
        df = df.append(pd.read_csv(clinic_file), ignore_index = True)

    df = df.drop_duplicates(subset ="NCT Number")
    df = df.sort_values(by=['Start Date'], ascending=[False])
    df = df.reset_index()
    del df['Rank']
    del df['index']
    cols = df.columns
    print(cols)
    print(df)

    clinical_file = os.path.join(clinic_path, 'clinicalRetrieved' + '.csv')
    df.to_csv(clinical_file)
    print('clinicalMSC saved: ' + clinical_file)

    print("completed search_clinic")
