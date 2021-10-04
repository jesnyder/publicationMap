import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from c0100_search_resources import search_resources
from c0200_identify_gps_coordinates import identify_gps_coordinates
from c0300_aggregate_information import aggregate_information
from c0400_build_plots import build_plots
from c0500_build_gif import build_gif
from c0600_build_mp4 import build_mp4
from c0700_summarize_information import summarize_information

def main():
    """
    Map the publications by author affiliation and impact

    Tasks to complete:
    1. Search for relevant publications
    2. Find the latitude and longitude of author affiliations
    3. Aggregate information
    4. Make plot as .png
    5. Make .gif
    6. Make .mp4
    7. Summarize aggregated information

    """

    print("running main")

    # Review the note above
    # Identify which tasks need to be run
    # List the task numbers that need to be run below
    tasks = [5]

    if 1 in tasks: search_resources()
    if 2 in tasks: identify_gps_coordinates()
    if 3 in tasks: aggregate_information()
    if 4 in tasks: build_plots()
    if 5 in tasks: build_gif()
    if 6 in tasks: build_mp4()
    if 7 in tasks: summarize_information()

    print("completed main")

if __name__ == "__main__":
    main()
