from c0001_dim_image import dim_image

import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

def plot_df(df, monthIndex, monthYearList):
    """

    """

    minTime = monthYearList[0]
    maxTime = monthYearList[monthIndex]

    print("running plot_df")

    df = df.sort_values(by=['citations'], ascending=False)
    # print('df = ')
    # print(df)

    publishedYear = list(df['publishedYear'])
    publishedMonth = list(df['publishedMonth'])
    gpsLat = list(df['gpsLat'])
    gpsLong = list(df['gpsLong'])
    citations = list(df['citations'])
    monthsLapsed = list(df['monthsLapsed'])

    for i in range(len(gpsLat)): gpsLat[i] = float(gpsLat[i])
    for i in range(len(gpsLong)): gpsLong[i] = float(gpsLong[i])
    for i in range(len(citations)): citations[i] = float(citations[i])
    for i in range(len(publishedYear)): publishedYear[i] = float(publishedYear[i])
    for i in range(len(publishedMonth)): publishedMonth[i] = float(publishedMonth[i])


    figure, axes = plt.subplots()

    map_path = os.path.join('..', '..', 'blankMap')
    map_file = os.path.join(map_path, 'blankMap10' + '.png')
    img = plt.imread(map_file)
    # img = dim_image(img)

    #origin = [-180, 180, -90, 90]
    extent = [-180, 180, -90, 90]
    # axes.imshow(img, origin=origin, extent=extent)
    axes.imshow(img, extent=extent)



    for i in range(len(gpsLat)):

        xx = float(gpsLong[i])
        yy = float(gpsLat[i])
        rr = 10*citations[i]/monthsLapsed[i]*(monthIndex - (max(monthsLapsed)-monthsLapsed[i]))+1
        # print('xx, yy, rr = ' + str(xx) + ' , ' + str(yy) + ' , ' + str(rr))
        assert rr > 0

        colorMarker = [0, 0, 0]
        colorEdge = [0, 0, 0]
        for j in range(len(colorMarker)):

            if len(citations) > 2:
                variant = (max(citations) - citations[i]) / (max(citations) - min(citations))
                # variant = variant*(monthIndex - (max(monthsLapsed)-monthsLapsed[i]))/monthsLapsed[i]
                assert variant >=0 and variant <=1
            else:
                variant = 0.5

            variant = random.randint(0,50)
            variant = variant/50

            if citations[i]%3 == 0:
                if j == 0: colorMarker[j] = 1-0.5*variant
                if j == 1:  colorMarker[j] = 0
                if j == 2:  colorMarker[j] = 0.95

            if citations[i]%3 == 1:
                if j == 0: colorMarker[j] = 0
                if j == 1:  colorMarker[j] = 0.95
                if j == 2:  colorMarker[j] = 1-0.5*variant

            if citations[i]%3 == 2:
                if j == 0: colorMarker[j] = 0
                if j == 1:  colorMarker[j] = 1-0.5*variant
                if j == 2:  colorMarker[j] = 0.95

        colorEdge[j] = 0.85*colorMarker[j]

        plt.scatter(xx, yy, s = rr, color=colorMarker, edgecolors=colorEdge)

        axes.axis('off')
        plt.title( 'SI-Indexed Impact of Publications Citing RoosterBio Tech')

        path = os.path.join('..', '..', 'plots')
        if not os.path.isdir(path): os.mkdir(path)
        file = os.path.join(path, 'month' + str(monthIndex).zfill(2) + ".png")
        plt.savefig(file, bbox_inches='tight')


if __name__ == "__main__":
    main()
