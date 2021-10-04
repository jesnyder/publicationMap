from PIL import Image
import glob

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def make_mp4(blank_map_file_name):
    """

    """

    print('making gif')
    path = os.path.join('plots', blank_map_file_name)

    frames = []
    png_file = os.path.join(path, "*.png")

    path = os.path.join( 'gif')
    if not os.path.isdir(path): os.mkdir(path)
    save_file = os.path.join(path, 'publicationsMap' + '.gif')
    save_mp4 = os.path.join(path, 'publicationsMap' + '.mp4')

    clip = mp.VideoFileClip(save_file)
    clip.write_videofile(save_mp4)
