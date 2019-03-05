Global stitching Perkin Elmer Phenix Images  
==============================

This is a data science pipeline to allow for the reconstruction of stitched images from the Perkin Elmer Phenix instrument. Currently, images collected at 5x objective, and 1% overlap are mosaiced together using a python script.

This project is organized as a data-science pipeline to allow for faithful reconstruction of test-data for ease of understanding how this function works. At least, I hope!


Project Organization
--------------------

    .
    ├── AUTHORS.md
    ├── LICENSE
    ├── README.md
    └── src
        ├── tools
        └── visualization


Calling the function
--------------------
The function `PE_phenix_stack_stitcher.py` takes two arguments:
1) Input Path to Images Folder
2) Output Path to where stitched images go

The function is called from terminal/bash as such:

```console
foo@bar:~$ python3 OPZ20_stitch_images.py "Input Path" "Output Path"
```

Future Work
--------------------
1) Merge channels to make multi-stack TIFF
2) Flatfield Correction
3) Allowing for all sorts of images.
