from c0103_retrieve_ref import retrieve_ref
from c0106_test_map_size import test_map_size

import cv2
import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def test_map_extent(blank_map_file_name):
    """
    """

    print("running test_map_extent")

    e1s = np.arange(-174,-166,1)
    e2s = np.arange(185,194,1)
    e3s = np.arange(-62,-56,1)
    e4s = np.arange(108,112,1)

    #e1s = [-167]
    #e2s = [189]
    e3s = [-58]
    e4s = [108]

    for e1 in e1s:
        for e2 in e2s:
            for e3 in e3s:
                for e4 in e4s:

                    extent = [e1, e2, e3, e4]

                    print('extent = ')
                    print(extent)

                    test_map_size(blank_map_file_name, extent)
