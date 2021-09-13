from c0001_dim_image import dim_image
from c0002_plot_df import plot_df
from c0200_make_gif import make_gif

import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    """

    """

    print("running main")

    metadata_path = os.path.join('..', '..', 'metadata')
    print('metadata_path = ')
    print(metadata_path)
    metadata_file = os.path.join(metadata_path, 'publishedMetadata.csv')
    print('metadata_file = ')
    print(metadata_file)

    df = pd.read_csv(metadata_file)

    col_names = df.head()
    for name in col_names:
        if 'Unnamed' in name:
            del df[name]

    df = df.dropna()
    df = df.sort_values(by=['publishedYear' , 'publishedMonth'])

    gpsLat = list(df['gpsLat'])
    for i in range(len(gpsLat)): gpsLat[i] = float(gpsLat[i])

    # add months lapsed to each row
    monthsLapsedList = []
    for i in range(len(gpsLat)):
        monthsLapsed = (2021-float(df.iloc[i]['publishedYear'])-1)*12+9+(12-float(df.iloc[i]['publishedMonth']))
        monthsLapsedList.append(monthsLapsed)
    df['monthsLapsed'] = monthsLapsedList
    monthsLapsed = list(df['monthsLapsed'])

    print('df = ')
    print(df)

    publishedYear = list(df['publishedYear'])
    for i in range(len(publishedYear)): publishedYear[i] = float(publishedYear[i])
    monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Aug', 'Oct', 'Nov', 'Dec']
    minPubYear = str(int(min(publishedYear)))
    minMonthIndex = int(df.iloc[0]['publishedMonth'])-1
    minPubMonth = monthList[minMonthIndex]
    monthYearList = []
    for i in range(int(max(monthsLapsed))):

        monthName = monthList[int((i+minMonthIndex)%12)]
        print('monthName = ' + str(monthName))
        yearName =  int(minPubYear) + int((i+minMonthIndex)/12)
        monthYearList.append(str(monthName + ' ' + str(yearName)))

    # print('monthYearList = ')
    # print(monthYearList)

    # df['monthYear'] = monthYearList
    metadata_file = os.path.join(metadata_path, 'metadata' + '_' + str('editted') + '.csv')
    df.to_csv(metadata_file)


    for i in range(int(max(monthsLapsed))):

        month = max(monthsLapsed)-i

        df_monthly = df.drop(df[df['monthsLapsed'] < month].index)

        currentMonth = 12-int((month+minMonthIndex-1)%12)
        currentYear = max(list(df_monthly['publishedYear']))
        monthYearList = str( str(minMonthIndex) + '/' + str(minPubYear) + '-' + str(currentMonth) + '/' + str(currentYear))

        plot_df(df_monthly, i, monthYearList)

        print('% complete = ' + str(i/max(monthsLapsed)))

    make_gif()


if __name__ == "__main__":
    main()
