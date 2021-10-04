import requests
import urllib.parse
import os
from os.path import exists
import pandas as pd


def findLatLong(sourceFile, saveFile):
    """
    Add two columns to a structured dataset for lat and long of an address
    """

    df = pd.read_csv(sourceFile)
    del df['Unnamed: 0']

    df = df.dropna(subset=['Address'])
    addresses = list(df['Address'])

    lats, lons = [], []
    for address in addresses:
        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'
        # print('url = ')
        # print(url)

        print('url = ')
        print(url)
        print('address = ')
        print(address)

        response = requests.get(url).json()
        # print('response = ')
        # print(response)

        print(response[0]["lat"])
        print(response[0]["lon"])

        lat = response[0]["lat"]
        lon = response[0]["lon"]

        lats.append(lat)
        lons.append(lon)
        #df.loc[len(df.index)] = [address, lat, lon]
        #print('df = ')
        #print(df)

    df['gpsLat'] = lats
    df['gpsLong'] = lons

    print('df = ')
    print(df)

    df.to_csv(saveFile)
    print('gps saved: ' + saveFile)

    print('completed findLongLat')
