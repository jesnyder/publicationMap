
from bs4 import BeautifulSoup

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pypatent
import requests

from c0104_findLatLong import findLatLong

def search_pubs():
    """
    Objective: List Rooster publication with metadata

    Task 1: Identify search terms for google scholar
    Task 2: Query
    Task 3: Structure data
    """

    print("running search_pubs")

    search_terms = []
    search_terms.append('RoosterBio')
    search_terms.append('Multivascular networks and functional intravascular topologies within biocompatible hydrogels')
    search_terms.append('Mesenchymal Stem Cell Perspective: Cell Biology to Clinical Progress')
    search_terms.append('Mesenchymal Stromal Cell Exosomes Ameliorate Experimental Bronchopulmonary Dysplasia and Restore Lung Function through Macrophage Immunomodulation')
    search_terms.append('Bone marrow-derived from the human femoral shaft as a new source of mesenchymal stem/stromal cells: an alternative cell material for banking and clinical')
    search_terms.append('Rooster Basal-MSC')
    search_terms.append('Rooster Nourish')
    search_terms.append('Rooster MSC')

    # Step 2: Scrape
    # SerpApi search can only be done once a month
    # search_serpapi(search_terms)

    # Step 3: Structure data
    # Parse the html to list all publications
    parse_html()

    # Step 4: Find GPS find gps coordinates
    unique_addresses()

    #





def search_serpapi(search_terms):
    """
    Query serapapi
    Save in a text file
    """

    results = ''

    for term in search_terms:

        startNums = np.arange(0,50,2)
        if len(term) > 30: startNums = np.arange(0,2,1)

        for starts in startNums:
            params = {
                "api_key": "7d88bc0429b4b4cf729d976c37c3bec730cf2caa3887e90c7cd7c56f707636f1",
                "engine": "google_scholar",
                "q": term,
                "hl": "en",
                "as_ylo": "2012",
                "as_yhi": "2022",
                "start": starts*10,
                "num": starts*10+20,
            }

            search = GoogleSearch(params)
            result = search.get_dict()

            errorMessage = 'Your searches for the month are exhausted. You can upgrade plans on SerpApi.com website.'
            if errorMessage in str(results): print('Error found:' + errorMessage)

            errorMessage = 'Google hasn\'t returned any results for this query.'
            if errorMessage in str(results): print('Error found:' + errorMessage)

            if errorMessage not in str(results):
                results = results + ' ' + str(result)

    df = pd.DataFrame()
    df['text'] = [results]

    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    pub_path = os.path.join('searchResults')
    if not os.path.isdir(pub_path): os.mkdir(pub_path)
    pub_path = os.path.join('searchResults', 'pubs')
    if not os.path.isdir(pub_path): os.mkdir(pub_path)
    pub_path = os.path.join('searchResults', 'pubs', 'scrapeSerpapi')
    if not os.path.isdir(pub_path): os.mkdir(pub_path)

    pub_file = os.path.join(pub_path, 'pubsRetrieved' + '_' + str(time)  + '.csv')
    df.to_csv(pub_file)

    print('pubs saved: ' + pub_file)

    print("completed search_pubs")


def parse_html():
    """

    """

    pubSource = []
    pub_path = os.path.join('searchResults', 'pubs', 'saved')
    arr = os.listdir(pub_path)
    for path in arr: pubSource.append(os.path.join(pub_path, path))

    pub_path = os.path.join('searchResults', 'pubs', 'scrapeSerpapi')
    arr = os.listdir(pub_path)
    for path in arr: pubSource.append(os.path.join(pub_path, path))

    # print('pubSource = ')
    # print(pubSource)

    textFull = ''

    for file in pubSource:

        with open(file, newline='') as csvfile:
            for row in csvfile:
                textFull = textFull + ' ' + row

    positionSplit = textFull.split('{\'position\':')

    tags = []
    tags.append('titlePaper|\'title\': \'|\', \'')
    tags.append('citations|\'cited_by\': {\'total\': |, \'')
    tags.append('url| \'html_version\': \'|\'')
    tags.append('scholarUrl|, \'link\': \' |\', \'cites_id\'')
    tags.append('snippet| \'snippet\': \'|\', \'pu')
    tags.append('info| \'publication_info\': |, \'resources\'')
    tags.append('article| | ')

    df = pd.DataFrame()
    for tag in tags:

        list = []
        for article in positionSplit:

            tagTitle, tagBegin, tagEnd = tag.split('|')
            articleSplit = article.split(tagBegin)

            if len(articleSplit) > 1:
                articleSecondSplit = articleSplit[1]
                articleThirdSplit = articleSecondSplit.split(tagEnd)
                target = articleThirdSplit[0]

            else: target = ''

            if tagTitle == 'article': target = str(article)
            if tagTitle == 'citations':
                if len(target) > 0: target = int(target)
                else: target = 0

            list.append(target)

        df[tagTitle] = list

    df = df.sort_values(by=['citations'], ascending=False)
    df = df.drop_duplicates(subset=['titlePaper', 'citations'])
    df = df.reset_index()
    del df['index']
    print(df)

    pub_path = os.path.join('searchResults', 'pubs')
    if not os.path.isdir(pub_path): os.mkdir(pub_path)
    pub_file = os.path.join(pub_path, 'pubsRooster'  + '.csv')
    df.to_csv(pub_file)
    print('pubs saved: ' + pub_file)


def unique_addresses():
    """
    List unique addresses
    with the frequency they occur
    and latitude / longitude
    """

    pub_path = os.path.join('searchResults', 'pubs', 'manuallyCollected')
    pub_file = os.path.join(pub_path, 'manuallyCollectedPubData'  + '.csv')
    df = pd.read_csv(pub_file)

    addresses = list(df['Address'])

    address_unique, address_counts = [], []

    for address in addresses:

        if address not in address_unique:

            df_address = df.drop(df[df.Address != address].index)
            address_specific = list(df_address['Address'])

            address_unique.append(address)
            address_counts.append(len(address_specific))

    df_address = pd.DataFrame()
    df_address['Address'] = address_unique
    df_address['Publications'] = address_counts
    df_address = df_address.sort_values(by=['Publications'], ascending=False)

    pub_path = os.path.join('searchResults', 'pubs')
    pub_file = os.path.join(pub_path, 'pubsAddressUnique'  + '.csv')
    df_address.to_csv(pub_file)

    sourceFile = pub_file
    saveFile = os.path.join(pub_path, 'pubsAddressUniqueLatLong'  + '.csv')
    findLatLong(sourceFile, saveFile)

    print(df_address)
