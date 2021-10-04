import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pypatent

def search_patent():
    """
    Find Rooster cumstomers in the patent databases
    Find all operators in the mesenchymal/exosome sector
    Identify operators not citing Rooster
    """

    print("running search_patents")

    # Name searchers
    searchNames = []
    searchNames.append('Rooster') # Identify product adoption
    searchNames.append('MSC') # Identify domain space

    for name in searchNames:

        # help on USPTO search terms
        # https://patft.uspto.gov/netahtml/PTO/help/helpflds.htm
        if name == 'Rooster': searchTerms = ['RoosterBio', 'Rooster Nourish',
                'SPEC/RoosterBio', 'SPEC/Rooster Nourish']

        elif name == 'MSC': searchTerms = ['mesenchymal', 'exosome']

        query_USPTO(name, searchTerms)

    # Find the patents that do not cite Rooster technology
    find_not_rooster(searchNames)

    print("completed search_patents")



def query_USPTO(searchName, searchTerms):
    """
    Query the USPTO with the search terms
    Save as a dataframe
    """
    df = pd.DataFrame()

    for term in searchTerms:
        df1 = pypatent.Search(term).as_dataframe()
        df = df.append(df1, ignore_index = True)

    df = df.drop_duplicates(subset ="title")
    df = df.sort_values(by=['patent_date'], ascending = False)
    df = df.reset_index()
    del df['index']
    print(df)

    patent_path = os.path.join('searchResults')
    if not os.path.isdir(patent_path): os.mkdir(patent_path)
    patent_path = os.path.join('searchResults', 'patents')
    if not os.path.isdir(patent_path): os.mkdir(patent_path)
    patent_file = os.path.join(patent_path, 'patents' + searchName + '.csv')
    df.to_csv(patent_file)
    print('patentsRetrieved saved: ' + patent_file)


def find_not_rooster(searchNames):
    """

    """
    patent_path = os.path.join('searchResults', 'patents')

    df = pd.DataFrame()

    patent_file = os.path.join(patent_path, 'patents' + searchNames[0] + '.csv')
    df_rooster = pd.read_csv(patent_file)
    titleRooster = list(df_rooster['title'])
    print('titleRooster has entries: ' + str(len(titleRooster)))

    patent_file = os.path.join(patent_path, 'patents' + searchNames[1] + '.csv')
    df_msc = pd.read_csv(patent_file)
    df = df_msc
    titleMSC = list(df_msc['title'])
    print('titleMSC has entries: ' + str(len(titleMSC)))

    for title in titleMSC:

        if title in titleRooster:

            df = df.drop(df[df.title == title].index)

    for title in titleRooster:
        if title not in titleMSC:
            print('title found not in MSC: ' + str(title))

    starts = list(df['patent_date'])

    for start in starts:
        startSplit = start.split(',')
        year = int(startSplit[1])
        if year < 2012:
            df = df.drop(df[df['patent_date'] == start].index)


    cols = df.columns
    print(cols)
    del df['Unnamed: 0']
    df = df.sort_values(by=['patent_date'], ascending = False )
    df = df.reset_index()
    del df['index']

    print(df)

    patent_file = os.path.join(patent_path, 'patents' + 'NotRooster' + '.csv')
    df.to_csv(patent_file)
