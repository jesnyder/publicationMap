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

    print('df = ')
    print(df)

    gpsLat = list(df['gpsLat'])
    gpsLong = list(df['gpsLong'])
    citations = list(df['citations'])

    for i in range(len(gpsLat)): gpsLat[i] = float(gpsLat[i])
    for i in range(len(gpsLong)): gpsLong[i] = float(gpsLong[i])
    for i in range(len(citations)): citations[i] = float(citations[i])

    figure, axes = plt.subplots()


    map_path = os.path.join('..', '..', 'blankMap')
    map_file = os.path.join(map_path, 'blankMap' + '.png')
    print('map_file = ')
    print(map_file)
    origin = [-0.5, 6.5, -0.5, 5.5]
    img = plt.imread(map_file, origin=origin)
    # fig, ax = plt.subplots()
    axes.imshow(img)


    for i in range(len(gpsLat)):

        xx = float(gpsLong[i])
        yy = float(gpsLat[i])
        rr = 10*float(citations[i])
        print('xx, yy, rr = ' + str(xx) + ' , ' + str(yy) + ' , ' + str(rr))

        colorMarker = [0.5, 0, 0]
        colorEdge = [0.5, 0, 0]
        for j in range(len(colorMarker)):
            variant = (max(citations) - citations[i]) / (max(citations) - min(citations))
            if j == 0: colorMarker[j] = variant
            elif j == 1:  colorMarker[j] = 0
            elif j == 2:  colorMarker[j] = 1- variant
            colorEdge[j] = 0.5*colorMarker[j]

            print('colorMarker / colorEdge = ')
            print(colorMarker)
            print(colorEdge)

        plt.scatter(xx, yy, s = rr, color=colorMarker, edgecolors=colorEdge)

    plt.title( 'Colored Circle' )

    path = os.path.join('..', '..', 'plots')
    if not os.path.isdir(path): os.mkdir(path)
    file = os.path.join(path, 'test' + ".png")
    plt.savefig(file, bbox_inches='tight')

if __name__ == "__main__":
    main()
