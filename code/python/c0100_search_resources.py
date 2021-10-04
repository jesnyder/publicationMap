import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from c0101_search_patent import search_patent
from c0102_search_clinic import search_clinic
from c0103_search_pubs import search_pubs

def search_resources():
    """
    Identify a query
    Search databases
    Save organized data into dataframe
    """

    print("running search_resources")

    # Write the resources to search in the list below
    # Options include:
    # patent = search US Patent and Trademark Databased
    # clinic = search NIH Clinical Trial Database - International

    databases = []
    databases.append('patent')
    databases.append('clinic')
    databases.append('pubs')

    if 'patent' in databases: search_patent()
    if 'clinic' in databases: search_clinic()
    if 'pubs' in databases: search_pubs()



    print("completed search_resources")
