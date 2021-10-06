from PIL import Image
import glob

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from c0001_retrieve_ref import retrieve_ref

def build_gif():
    """

    """

    blank_map_file_name = 'blankMap17'
    plot_dpi = retrieve_ref('plot_dpi')

    print('building gif')
    path = os.path.join('plots', blank_map_file_name, str(int(plot_dpi)))

    frames = []
    png_file = os.path.join(path, "*.png")

    path = os.path.join( 'gif', blank_map_file_name)
    if not os.path.isdir(path): os.mkdir(path)
    save_file = os.path.join(path, 'publicationsMap_' + str(int(plot_dpi))  + '.gif')

    imgs = glob.glob(png_file)
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

        # Save into a GIF file that loops forever
        frames[0].save(save_file, format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=300, loop=0)
