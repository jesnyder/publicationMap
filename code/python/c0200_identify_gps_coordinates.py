from PIL import Image
import glob

import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from c0104_findLatLong import findLatLong

def identify_gps_coordinates():
    """

    """

    print("running identify_gps_coordinates")

    pub_path = os.path.join('searchResults', 'pubs')
    pub_file = os.path.join(pub_path, 'pubsAddressUnique'  + '.csv')
    sourceFile = pub_file
    saveFile = os.path.join(pub_path, 'pubsAddressUniqueLatLong'  + '.csv')
    findLatLong(sourceFile, saveFile)


    print("completed identify_gps_coordinates")
