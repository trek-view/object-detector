# Object Detector 

## In one sentence

Command line Python script that 1) directory of images, 2) identifies objects in the image, 3) writes a json document with the identified objects and their position in each image.

## Why we built this

We capture millions of images every year. Manually tagging each one with the objects inside it is a time consuming job.

To reduce the human effort of helping understand and log what we've captured in our images, we wanted a tool that could do it automatically.

Object Detector is the result of that goal.

## How it works

### Overview

1. You define a directory of photos
2. The script attempts to identify objects withing them
3. If any object is identified the script records the object classification and location in the image
4. And finally writes out a json document with the identified objects and their position in each image

## Requirements

### OS Requirements

Works on Windows, Linux and MacOS.

### Software Requirements / Installation

We have tested this script on Python version 3.7.6-amd64.

The following modules are required

* `pip install opencv-python`
* `pip install tensorflow==1.15`
* `pip install keras==2.3.1`
* `pip install imageai`

You must also download the model file [resnet50_coco_best_v2.0.1.h5](https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0) and place in the `models` directory in this repository.

* [exiftool](https://exiftool.org/) needs to be installed on the system. If used on Windows, download the stand-alone .exe executable. Rename the .exe file to `exiftool.exe`. Put the .exe file in the same folder as the repo.

The `.ExifTool_Config` ([.ExifTool_Config explanation](https://exiftool.org/faq.html#Q11)) needs be in the HOME directory (Mac, Linux) or in the same folder as the repo (Windows)

## Usage

```
python object-detector.py [INPUT_DIR] [MIN_PERCENTAGE_PROBABILITY]
```

Where `[INPUT]` is a directory of image files you want to identify objects in.

`[MIN_PERCENTAGE_PROBABILITY]` is the minimum % probability accepted for object detection.

Accepts values between 1 (highest probability) and 100 (lowest probability). Recommended is 40.

```
python object-detector.py INPUT 50
```

For example, if you set to 50, you are saying the detection thinks there is 50% chance this object is what it has been classified as.

1 assumes 100% confidence (which is extremely unlikely).

Note, the lower the value entered the more intensively objects will be analysed, and thus the longer the script will take to run.

[The model currently analyses for the objects listed here](/objects.txt).

The output will provide a `.json` document (with the same name as the input directory), listing the filename, the objects discovered in the image with their position.

```
[
    {
        "uploaded (1).jpg": [
            { "car": [2312, 1379, 2519, 1528] },
            { "car": [3021, 1350, 3294, 1503] },
            { "car": [2167, 1430, 2380, 1602] },
            { "car": [1866, 1426, 2128, 1701] },
            { "car": [1, 1606, 175, 1727] },
            { "car": [311, 1598, 475, 1679] },
            { "car": [451, 1599, 663, 1703] },
            { "car": [651, 1610, 895, 1742] },
            { "car": [770, 1609, 1043, 1755] },
            { "car": [839, 1599, 1166, 1776] },
            { "car": [1204, 1559, 1523, 1789] },
            { "car": [1494, 1483, 1859, 1783] },
            { "car": [3100, 1439, 3747, 1852] },
            { "car": [3741, 1517, 4323, 2033] }
        ]
    },
    { "uploaded (2).jpg": [{ "person": [2364, 1623, 2489, 1979] }] },
    {
        "uploaded (14).jpg": [
            { "person": [5109, 1537, 5276, 1975] },
            { "person": [5608, 1556, 5732, 1876] },
            { "person": [1139, 1773, 1410, 1976] },
            { "person": [101, 1948, 408, 2200] },
            { "bicycle": [3091, 1747, 3641, 2180] },
            { "bicycle": [3099, 1728, 4198, 2270] }
        ]
    }
  ]
```

Position is defined as coordinate 4 values. These are the pixel position of a rectangle in which the object resides (`[left, top, right, bottom]`).

For example,

```
"person": [5109, 1537, 5276, 1975]
```

Means the script detected a person between the 5109 and 5276 pixel (from left to right) and between the 1537 and 1975 pixels (top to bottom) in this image.

And the coordinate of a point at right and bottom of the rectangle.

## Support 

We offer community support for all our software on our Campfire forum. [Ask a question or make a suggestion here](https://campfire.trekview.org/c/support/8).

## License

Objector Detector is licensed under a [GNU AGPLv3 License](/LICENSE.txt).