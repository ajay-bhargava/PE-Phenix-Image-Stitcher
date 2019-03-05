#!/usr/bin/python

'''

def stitch_images(input_path, output_path)

    input_path: path to raw data collected from Phenix Database Output. This path should include
    output_path: path to where you want stitched images to go, this should be a previously defined directory

Creator: Ajay Bhargava
Date: 03/03/19

'''


import sys

def stitch_images(path_to_files, output_path, *args):
    from xml_parser import parse_phenix_xml as parse_xml
    from tqdm import tqdm
    from image_stitcher import channel_stitch
    from skimage.external import tifffile

    path_to_xml_file = path_to_files + 'Index.idx.xml'
    dictionary = parse_xml(path_to_xml_file)

    for wells in tqdm(dictionary):
        d = {channels:images for channels,images in dictionary[wells].items()}
        stitching_input = [(wells, channels, images) for channels, images in d.items()]
        stitched_list = [channel_stitch(path_to_files, stitching_input[index][0], stitching_input[index][1], stitching_input[index][2]) for index, item in enumerate(stitching_input)]
        with tifffile.TiffWriter(output_path + wells + "_" + "image_stack.tiff", imagej = True) as stack:
            for item in stitched_list:
                stack.save(item, photometric='minisblack')

if __name__ == "__main__":
    stitch_images(path_to_files = sys.argv[1], output_path = sys.argv[2])
