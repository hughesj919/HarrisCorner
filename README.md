#Harris Corner Detector
####Jordan Hughes
####UC Santa Barbara
####hughesj919 at gmail.com

This is a python based harris corner detector.  OpenCV module is used to read images in

Usage example is as follows:

```python Corners.py —-window_size 5 —-k_corner_response .04 —-corner_threshold 10000 checkerboard.png```

The script will run and print some parameter values for verification purposes. 
For more help with the code run ```pydoc HarrisCorner``` at a terminal.  The script will run and output a few parameters for validation purposes. 
File output will be:

* finalimage.png — This will be an image with red boxes of window size indicating corner detection
* corners.txt — A list of the top 100 corners with the highest corner response values, r.

A Harris Corner Detector

Corner detection in images has many applications ranging from panoramic stitching to tracking to object recognition. This
is a simple script that implements a Harris Corner detection algorithm.  For more information on the algorithm itself, 
see the following links:

* [Harris Corner Detector Lecture](http://www.cse.psu.edu/~rtc12/CSE486/lecture06.pdf)
* [Harris and Stephens Corner Detection Wiki](https://en.wikipedia.org/wiki/Corner_detection#The_Harris_.26_Stephens_.2F_Plessey_.2F_Shi.E2.80.93Tomasi_corner_detection_algorithm)
* [A Combined Corner and Edge Detector](http://www.bmva.org/bmvc/1988/avc-88-023.pdf)

####This is our original image:

![Checkerboard Original](/Images/checkerboard.png)

####This is our final image:
![Checkerboard Final](/Images/finalimage.png)