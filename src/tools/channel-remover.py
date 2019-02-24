
'''

By Ajay Bhargava
def channel_remover()
A function to remove unneeded channels from existing stitched files produced.

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
