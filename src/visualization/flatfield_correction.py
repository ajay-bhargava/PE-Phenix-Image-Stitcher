#!/usr/bin/python

'''

def flatfield_correction_algorithm(input_glob, known_img, output_path)

    input_glob: is a glob './*.tiff' of files to be processed
    known_img: path of known image where acquisition was performed but no sample. known_img posesses the the same artifacts as the experimental images
    output_path: where to store the files when the job is done

    Caution: Large images will cause this algorithm to be slow

Creator: Ajay Bhargava
Date: 18/02/19

'''

def flatfield_correction_algorithm(glob_path, known_img_path, output_path):
    # Import libraries
    import tifffile as tiff
    import numpy as np
    import glob as glob
    from tqdm import tqdm

    known = tiff.imread(known_img)

    #
    for file in tqdm(sorted(glob.glob(glob_path))):
        img = tiff.imread(file)
        d,w,h = (img.shape[0], img.shape[1], img.shape[2])
        img_new = np.zeros((d,w,h), dtype = uint8)
        for z in range(0, d):
            for y in range(0, h):
                for x in range(0, w):
                    img_new[z,x,y] = (((img[z,x,y] - 0) * (np.mean(known[z,:,:])))/(known[z,x,y] - 0))
    return img_new
#

# Testing the function.
