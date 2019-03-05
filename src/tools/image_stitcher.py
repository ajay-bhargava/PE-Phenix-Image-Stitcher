'''

def channel_stitch(path to files, wells, channel, images):
    This is an internal function used with main function
    To accomodate resolution of images at different magnification, please adjust the mosaic.paste to accomodate for this

    By: Ajay Bhargava
    03/03/19

'''


def channel_stitch(path_to_files, wells, channel, images):
    from PIL import Image
    import numpy
    open_img_container = []
    for i, current in enumerate(images):
        open_img_container.append(Image.open(path_to_files + current))
    mosaic = Image.new('L', (3240,3240))
    mosaic.paste(open_img_container[1], (0,0))
    mosaic.paste(open_img_container[2], (1080,0))
    mosaic.paste(open_img_container[3], (2160,0))
    mosaic.paste(open_img_container[5], (0,1080))
    mosaic.paste(open_img_container[0], (1080,1080))
    mosaic.paste(open_img_container[4], (2160,1080))
    mosaic.paste(open_img_container[6], (0,2160))
    mosaic.paste(open_img_container[7], (1080,2160))
    mosaic.paste(open_img_container[8], (2160,2160))
    numpy_array = numpy.array(mosaic)
    return (numpy_array)
#
