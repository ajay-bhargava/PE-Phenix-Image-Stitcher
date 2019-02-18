
'''

def channel_remover()
By Ajay Bhargava
A function to remove flatfield issues 

'''

def channel_remover(glob_path):
    # Import libraries
    import tifffile as tiff
    import numpy as np
    import glob as glob
    from skimage import io as io

    # Import images
    tf = [tiff.imread(file) for file in sorted(glob.glob(glob_path))]
    tf_np = [np.array(tiff) for tiff in tf]
    #

# Clear
