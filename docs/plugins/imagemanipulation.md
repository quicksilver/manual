#Image Manipulation

Actions to scale and change format of images.

 Summary                  | &nbsp; 
-------------------------:|:--------------------
 Latest plugin version    | 1.1.1
 Supported MacOS versions | 10.11, 10.12, 10.13
 Quicksilver builds       | 4024


## Overview

Actions to scale, change the format of images. Both actions take an argument
in Quicksilver's 3rd pane. Examples can be seen below.

## Actions

Scale Image…

    This method allows you to scale an image selected in Quicksilver's 1st pane. Various scaling and format options are available, and are listed below.
Save Image in Format…

    Saves the image in the format specified. Valid formats include: `tif`, `png`, `gif`, `bmp`, `jpg` (or `jpeg`), `jpg2` (or `jpeg2`)

### Scaling Syntax

The basic format for the string is (terms in square brackets are optional):

    
    
    SCALING_INFORMATION [as FORMATTING_INFORMATION]
    

where `SCALING_INFORMATION` has the format:

    
    
    [fit] WIDTH [x HEIGHT]
    

with `WIDTH` and `HEIGHT` defined as whole numbers in terms of pixels. For
example, "210" means "210px", but it is also possible to type "210px".

`FORMATTING_INFORMATION` has the format:

    
    
    JPG/PNG/GIF/TIFF [low/med/hi] [prog(ressive)] [inter(laced)]
    

which allows you to set the file type, quality of the image and various
further options (progressive for `.jpg` files and interlaced for `.png`
files).

Examples:

80%

    Scales an image to 80% of the original image, keeping the same file format as the input image.
500px x 50px

    Scales the image to be 500px in width by 50px in height. The format is kept the same as the original.
x200 as gif

    Scales the image to be 200px in height, maintaining the width so as to scale the image. Saves the result as a GIF file.
fit 640x480 as jpg high progressive

    Creates a JPEG image that will fit within a 640x480 rectangle and is of high quality with progressive enabled.
50% as interlaced png

    Creates a PNG with dimensions half of the original.

## Trigger Events

Event Triggers can be run when images are resized or reformatted by this plug-
in. For both actions, the "Event Trigger Object" will refer to the new image
file(s).