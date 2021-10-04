from c0103_retrieve_ref import retrieve_ref

import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def test_map_size(blank_map_file_name, extent):
    """
    """

    print("running test_map_size")

    plt.close('all')
    figure, axes = plt.subplots()

    map_path = os.path.join('blankMap')
    map_file = os.path.join(map_path, blank_map_file_name + '.png')
    img = plt.imread(map_file)

    """
    extent = [-180, 180, -90, 90]

    if '17' in blank_map_file_name:
        extent = [-180, 180, -50, 90]
    """


    img = cv2.imread(map_file)
    axes.imshow(img, extent=extent)

    axes.axis('off')
    plt.title( 'SI-Indexed Impact of RoosterBio Tech: ')

    gpsLat = np.arange(-90,100,10)
    gpsLong = np.arange(-180,200,20)
    floridaLat, floridaLong = 25.26240780152312, -80.56288557485856
    ausLat, ausLong = -17.05906897210599, 140.1524453879447
    fuegoLat, fuegoLong = -55.13001467952586, -67.09364723055118
    seatLat, seatLong = 48.27464770443345, -124.53467764106274
    singLat, singLong = 1.3181149401422625, 103.818831724967

    for i in range(len(gpsLat)):

        xx = float(gpsLong[i])
        yy = float(gpsLat[i])
        rr = 1

        colorOrange = [240/255, 83/255, 35/255]
        colorPurple = [23/255, 27/255, 96/255]
        colorBlueDark = [0/255, 153/255, 216/255]
        colorBlueLight = [0/255, 188/255, 231/255]
        colorGray = [233/255, 225/255, 223/255]

        colorMarker = colorPurple
        colorEdge = colorBlueLight

        plt.plot([-180, 0, 180], [0, 0, 0],  linewidth=0.1)
        plt.plot([0, 0, 0], [-90, 0, 90],  linewidth=0.1)

        scatterTransparency = retrieve_ref('scatterTransparency')
        scatterTransparency = 0.8
        plt.scatter(xx, yy, s = rr, color=colorMarker, alpha=float(scatterTransparency), edgecolors=colorEdge, linewidths=0.1)

        colorMarker = colorOrange
        colorEdge = colorBlueLight

        plt.scatter(floridaLong, floridaLat, s = rr, color=colorMarker, alpha=float(scatterTransparency), edgecolors=colorEdge, linewidths=0.1)
        plt.plot([floridaLong, floridaLong, floridaLong], [-90, 0, 90],  linewidth=.01)
        plt.plot([-180, 0, 180], [floridaLat, floridaLat, floridaLat],  linewidth=.01)

        plt.scatter(ausLong, ausLat, s = rr, color=colorMarker, alpha=float(scatterTransparency), edgecolors=colorEdge, linewidths=0.1)
        plt.plot([ausLong, ausLong, ausLong], [-90, 0, 90],  linewidth=.1)
        plt.plot([-180, 0, 180], [ausLat, ausLat, ausLat],  linewidth=.01)

        plt.scatter(fuegoLong, fuegoLat, s = rr, color=colorMarker, alpha=float(scatterTransparency), edgecolors=colorEdge, linewidths=0.1)
        plt.plot([fuegoLong, fuegoLong, fuegoLong], [-90, 0, 90],  linewidth=0.01)
        plt.plot([-180, 0, 180], [fuegoLat, fuegoLat, fuegoLat],  linewidth=.01)

        plt.scatter(seatLong, seatLat, s = rr, color=colorMarker, alpha=float(scatterTransparency), edgecolors=colorEdge, linewidths=0.1)
        plt.plot([seatLong, seatLong, seatLong], [-90, 0, 90],  linewidth=0.01)
        plt.plot([-180, 0, 180], [seatLat, seatLat, seatLat],  linewidth=.01)

        plt.scatter(seatLong, seatLat, s = rr, color=colorMarker, alpha=float(scatterTransparency), edgecolors=colorEdge, linewidths=0.1)
        plt.plot([singLong, singLong, singLong], [-90, 0, 90],  linewidth=0.01)
        plt.plot([-180, 0, 180], [singLat, singLat, singLat],  linewidth=.01)



        plt.scatter([0], [0], s = rr, color=colorMarker, alpha=float(scatterTransparency), edgecolors=colorEdge, linewidths=0.1)

    extent_name = '_'
    for e in extent:
        extent_name = extent_name + str(e) + '_'

    path = os.path.join('plots', 'test', blank_map_file_name)
    if not os.path.isdir(path): os.mkdir(path)
    file = os.path.join(path, 'month' + 'test' + extent_name+ ".png")

    plot_dpi = retrieve_ref('plot_dpi')
    plot_dpi = 150
    plt.savefig(file, bbox_inches='tight', dpi=plot_dpi)
    print('plot saved: ' + file)
