from PIL import Image
import glob

import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def make_gif():
    """

    """

    print('making gif')
    path = os.path.join('..', '..', 'plots')
    # file = os.path.join(path, 'month' + str(monthIndex).zfill(2) + ".png")

    # Create the frames
    #source_path = os.path.join('..', '..', 'plots')
    #source_files = os.listdir(source_path)


    frames = []
    png_file = os.path.join(path, "*.png")
    # print('png_file = ')
    # print(png_file)

    imgs = glob.glob(png_file)
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

        # Save into a GIF file that loops forever
        path = os.path.join('..', '..', 'gif')
        if not os.path.isdir(path): os.mkdir(path)
        save_file = os.path.join(path, 'publicationsMap' + '.gif')

        frames[0].save(save_file, format='GIF',
               append_images=frames[1:],
               save_all=True,
               duration=400, loop=0)
