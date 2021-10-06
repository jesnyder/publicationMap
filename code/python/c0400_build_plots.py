from c0401_map_maker import map_maker

import os
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def build_plots():
    """

    """

    blank_map_file_name = 'blankMap17'

    print("running main")

    metadata_path = os.path.join( 'metadata')
    metadata_file = os.path.join(metadata_path, 'publishedMetadata.csv')
    # metadata_file = os.path.join(metadata_path, 'locations_defined.csv')
    df = pd.read_csv(metadata_file)

    col_names = df.head()
    for name in col_names:
        if 'Unnamed' in name:
            del df[name]

    # df = df.replace(np.NaN, 100, inplace=True)
    # df = df.replace('NaN', 100, inplace=True)
    df["titlePaper"].fillna("No Title", inplace = True)
    df = df.drop(df[df['titlePaper'] == "No Title"].index)
    df.fillna("0", inplace = True)
    df = df.drop(df[df['count'] == "0"].index)
    print(df)

    # df = df.dropna()

    df = df.sort_values(by=['publishedYear' , 'publishedMonth'])
    minPubMonth = int(df.iloc[0]['publishedMonth'])
    minPubYear = int(df.iloc[0]['publishedYear'])
    print('Earliest Publication Date: ' + str(minPubMonth) + '/' + str(minPubYear))

    gpsLat = list(df['gpsLat'])
    for i in range(len(gpsLat)): gpsLat[i] = float(gpsLat[i])


    # add months lapsed to each row
    monthsLapsedList = []
    for i in range(len( list(df['gpsLat']))):

        if math.isnan(df.iloc[i]['publishedYear']) == False :
            monthsLapsed = (2021-float(df.iloc[i]['publishedYear'])-1)*12+9+(12-float(df.iloc[i]['publishedMonth']))
            monthsLapsedList.append(int(monthsLapsed))

        else: monthsLapsedList.append(np.nan)

    df['monthsLapsed'] = monthsLapsedList
    monthsLapsed = list(df['monthsLapsed'])

    df_saved = df.sort_values(by=['monthsLapsed'])
    metadata_file = os.path.join(metadata_path, 'metadata' + '_' + str('editted') + '.csv')
    df_saved.to_csv(metadata_file)

    monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for i in range(int(max(monthsLapsed))):

        month = max(monthsLapsed)-i
        df_monthly = df.drop(df[df['publishedYear'] < 2013].index)
        df_monthly = df.drop(df[df['monthsLapsed'] < month].index)

        currentMonth =  (i + minPubMonth)%12
        currentYear = int(minPubYear + int((i + minPubMonth-1)/12))
        # currentYear = max(list(df_monthly['publishedYear']))

        minPubMonthName = monthList[int(minPubMonth-1)]
        currentMonthName = monthList[int(currentMonth-1)]
        monthYearList = str( str(minPubMonthName) + ' ' + str(minPubYear) + '-' + str(currentMonthName) + ' ' + str(currentYear))

        map_maker(df_monthly, i, monthYearList, blank_map_file_name)

        print(monthYearList + '  | % complete = ' + str(100*round(i/max(monthsLapsed),2)))


if __name__ == "__main__":
    main()
