from c0001_retrieve_ref import retrieve_ref

import os
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random

def map_maker(df, monthIndex, monthYearList, blank_map_file_name):
    """

    """

    print("running plot_df")

    plot_dpi = retrieve_ref('plot_dpi')

    print('df = ')
    print(df)

    df = df.sort_values(by=['citations'], ascending=False)
    radius, reds, greens, blues = [], [], [], []
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

    map_path = os.path.join('blankMap')
    # map_file_name = str('blankMap' + str(14))
    map_file = os.path.join(map_path, blank_map_file_name + '.png')
    img = plt.imread(map_file)
    # img = dim_image(img)

    #origin = [-180, 180, -90, 90]
    extent = [-180, 180, -90, 90]

    if blank_map_file_name == 'blankMap17' or blank_map_file_name == 'blankMap18':

        extent = [-170, 190, -58, 108]

    # axes.imshow(img, origin=origin, extent=extent)
    axes.imshow(img, extent=extent)

    for i in range(len(gpsLat)):

        xx = float(gpsLong[i])
        yy = float(gpsLat[i])
        rr = (citations[i]+1)/monthsLapsed[i]*(monthIndex - (max(monthsLapsed)-monthsLapsed[i]))+1
        rr = 5*rr
        # rr = 1/3.14159*math.sqrt(rr)
        # print('xx, yy, rr = ' + str(xx) + ' , ' + str(yy) + ' , ' + str(rr))
        # print('rr = ' + str(rr))
        assert rr > 0

        colorOrange = [240/255, 83/255, 35/255]
        colorPurple = [23/255, 27/255, 96/255]
        colorBlueDark = [0/255, 153/255, 216/255]
        colorBlueLight = [0/255, 188/255, 231/255]
        colorGray = [233/255, 225/255, 223/255]

        colorMarker = [0, 0, 0]
        colorEdge = [0, 0, 0]
        for j in range(len(colorMarker)):

            if len(citations) > 2:
                variant = (max(citations) - citations[i]) / (max(citations) - min(citations))
                # variant = variant*(monthIndex - (max(monthsLapsed)-monthsLapsed[i]))/monthsLapsed[i]
                assert variant >=0 and variant <=1
            else:
                variant = 0.5

            variant = random.randint(-50,50)
            variant = variant/50

            colorRefValue = len(titleList[i])
            if colorRefValue%3 == 0:
                if j == 0: colorMarker[j] = colorOrange[0] + variant*0.1
                if j == 1:  colorMarker[j] = colorOrange[1] - variant*0.15
                if j == 2:  colorMarker[j] = colorOrange[2] + variant*0.15

            if colorRefValue%3 == 1:
                if j == 0:  colorMarker[j] = colorBlueDark[0] - variant*0.15
                if j == 1:  colorMarker[j] = colorBlueDark[1] + variant*0.15
                if j == 2:  colorMarker[j] = colorBlueDark[2] + variant*0.1

            if colorRefValue%3 == 2:
                if j == 0: colorMarker[j] = colorBlueLight[0] - variant*0.15
                if j == 1:  colorMarker[j] = colorBlueLight[1] + variant*0.15
                if j == 2:  colorMarker[j] = colorBlueLight[2] + variant*0.1

        for ii in range(len(colorMarker)):
            colorMarker[ii] = round(colorMarker[ii],4)
            if colorMarker[ii] > 1: colorMarker[ii] = 1
            elif colorMarker[ii] < 0: colorMarker[ii] = 0

        colorEdge[j] = 0.85*colorMarker[j]

        # print('colorMarker = ')
        # print(colorMarker)

        scatterTransparency = retrieve_ref('scatterTransparency')
        if citations[i] < 30: scatterTransparency = 0.8
        plt.scatter(xx, yy, s = rr, color=colorMarker, alpha=float(scatterTransparency), edgecolors=colorEdge, linewidths=0.1)

        radius.append(rr)
        reds.append(colorMarker[0])
        greens.append(colorMarker[0])
        blues.append(colorMarker[0])


    axes.axis('off')
    plt.title( 'SI-Indexed Impact of RoosterBio Tech: ' + monthYearList, fontname='sans-serif')

    path = os.path.join('plots')
    if not os.path.isdir(path): os.mkdir(path)
    path = os.path.join('plots', blank_map_file_name)
    if not os.path.isdir(path): os.mkdir(path)
    path = os.path.join('plots', blank_map_file_name, str(int(plot_dpi)))
    if not os.path.isdir(path): os.mkdir(path)
    file = os.path.join(path, 'month' + str(monthIndex).zfill(2) + ".png")

    plt.savefig(file, bbox_inches='tight', dpi=plot_dpi)


    df['radius'] = radius
    df['red'] = reds
    df['green'] = greens
    df['blue'] = blues

    path = os.path.join('dfMonthly')
    if not os.path.isdir(path): os.mkdir(path)
    file = os.path.join(path, 'month' + str(monthIndex).zfill(2) + ".csv")
    df.to_csv(file)

if __name__ == "__main__":
    main()
