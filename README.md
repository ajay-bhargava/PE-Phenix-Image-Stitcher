Global stitching Perkin Elmer Phenix Images  
===========================================

This is a data science pipeline to allow for the reconstruction of stitched images from the Perkin Elmer Phenix instrument. Currently, images collected at 5x objective, and 1% overlap are mosaic'ed together using this python script.

This project is organised as a data-science pipeline to allow for faithful reconstruction of test-data for ease of understanding how these function works. At least, I hope for you!

Happy to be tweeted @ajay_bhargava


Project Organization
--------------------

    .
    ├── AUTHORS.md
    ├── LICENSE
    ├── README.md
    └── data
        ├── raw (not included raw data, but keep it here)
    ├── reports
        ├── figures
    └── src
        ├── tools
        └── visualization (tools to do things with images once stitched)


Dependencies
------------
This package relies on the following dependencies:
`tqdm`,`PIL`, `numpy`, and `xml.etree`


Calling the function
--------------------
The function `PE_phenix_stack_stitcher.py` takes two arguments:
1) Input Path to Images Folder
2) Output Path to where stitched images go

The function is called from terminal/bash as such:

```console
foo@bar:~$ python3 PE_phenix_stack_stitcher.py "Input Path" "Output Path"
```

Getting the test data
---------------------
Unfortunately because my test data is unpublished, it still cannot be released for you on AWS at the moment. Ask me later.


Future Work (or your contribution)
----------------------------------

1) Trying to accommodate different kinds of images at different magnifications.
2) Doing time-lapse, multi-position (in the z-axis)
