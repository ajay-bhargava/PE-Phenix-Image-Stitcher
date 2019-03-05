#!/usr/bin/python

'''

def channel_remover(input_path):

    A function to remove unneeded channels from existing stitched files produced.
    Takes input arguments as a path of folders.

By Ajay Bhargava
Last Edit: 03/03/19

'''


def channel_remover(glob_path):
    # Import libraries
    import tifffile as tiff
    import numpy as np
    import glob as glob
    from tqdm import tqdm

    # Do function as a list comprehension or return each file
    tiff_cleaned = [np.delete(np.array(tiff.imread(file)), (2), axis = 0) for file in tqdm(sorted(glob.glob(glob_path)))]

# Finished function
