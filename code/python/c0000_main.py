from c0100_build_plots import build_plots
from c0200_make_gif import make_gif

import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    """

    """

    print("running main")

    # map citations per publications per month
    # build_plots()

    # build gif from plots
    make_gif()

    print("completed main")

if __name__ == "__main__":
    main()
