from c0101_dim_image import dim_image
from c0103_retrieve_ref import retrieve_ref

import os
import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

def plot_df(df, monthIndex, monthYearList):
    """

    """

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
    titleList = list(df['titlePaper'])

    for i in range(len(gpsLat)): gpsLat[i] = float(gpsLat[i])
    for i in range(len(gpsLong)): gpsLong[i] = float(gpsLong[i])
    for i in range(len(citations)): citations[i] = float(citations[i])
    for i in range(len(publishedYear)): publishedYear[i] = float(publishedYear[i])
    for i in range(len(publishedMonth)): publishedMonth[i] = float(publishedMonth[i])

    plt.close('all')
    figure, axes = plt.subplots()

    fontSize = retrieve_ref('fontSize')
    font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : fontSize}
    plt.rc('font', **font)
    plt.rc('font', size=fontSize)
    plt.rc('axes', titlesize=fontSize)

    map_path = os.path.join('..', '..', 'blankMap')
    map_file = os.path.join(map_path, 'blankMap14' + '.png')
    img = plt.imread(map_file)
    # img = dim_image(img)

    #origin = [-180, 180, -90, 90]
    extent = [-180, 180, -90, 90]
    # axes.imshow(img, origin=origin, extent=extent)
    axes.imshow(img, extent=extent)



    for i in range(len(gpsLat)):

        xx = float(gpsLong[i])
        yy = float(gpsLat[i])
        rr = citations[i]/monthsLapsed[i]*(monthIndex - (max(monthsLapsed)-monthsLapsed[i]))+1
        rr = 5*rr
        # rr = 1/3.14159*math.sqrt(rr)
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

            colorRefValue = len(titleList[i])
            if colorRefValue%3 == 0:
                if j == 0: colorMarker[j] = 1
                if j == 1:  colorMarker[j] = 1-0.5*variant
                if j == 2:  colorMarker[j] = 0

            if colorRefValue%3 == 1:
                if j == 0: colorMarker[j] = 1
                if j == 1:  colorMarker[j] = 0.75-0.5*variant
                if j == 2:  colorMarker[j] = 0.75*variant

            if colorRefValue%3 == 2:
                if j == 0: colorMarker[j] = 0
                if j == 1:  colorMarker[j] = 1-0.5*variant
                if j == 2:  colorMarker[j] = 0.99

        colorEdge[j] = 0.85*colorMarker[j]

        scatterTransparency = retrieve_ref('scatterTransparency')
        if citations[i] < 30: scatterTransparency = 0.8
        plt.scatter(xx, yy, s = rr, color=colorMarker, alpha=float(scatterTransparency), edgecolors=colorEdge, linewidths=0.1)

        axes.axis('off')
        plt.title( 'SI-Indexed Impact of RoosterBio Tech:' + monthYearList)

        path = os.path.join('..', '..', 'plots')
        if not os.path.isdir(path): os.mkdir(path)
        file = os.path.join(path, 'month' + str(monthIndex).zfill(2) + ".png")

        plot_dpi = retrieve_ref('plot_dpi')
        plt.savefig(file, bbox_inches='tight', dpi=plot_dpi)





if __name__ == "__main__":
    main()
