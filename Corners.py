"""


Usage example:
python corners.py --window_size 5 --k_corner_response 0.04 --corner_threshold 10000 checkerboard.png

"""
__author__ = 'jhughes'

import cv2
import numpy as np
import sys
import getopt
import operator

def readImage(filename):
    """
     Read in an image file, errors out if we can't find the file
    :param filename:
    :return: Img object if filename is found
    """
    img = cv2.imread(filename, 0)
    if img is None:
        print('Invalid image:' + filename)
        return None
    else:
        print('Image successfully read...')
        return img

def findCorners(img, window_size, k, thresh):
    """
    Finds and returns list of corners and new image with corners drawn
    :param img: The original image
    :param window_size: The size (side length) of the sliding window
    :param k: Harris corner constant. Usually 0.04 - 0.06
    :param thresh: The threshold above which a corner is counted
    :return:
    """
    #Find x and y derivatives
    dy, dx = np.gradient(img)
    Ixx = dx**2
    Ixy = dy*dx
    Iyy = dy**2
    height = img.shape[0]
    width = img.shape[1]

    cornerList = []
    newImg = img.copy()
    color_img = cv2.cvtColor(newImg, cv2.COLOR_GRAY2RGB)
    offset = window_size/2

    #Loop through image and find our corners
    print "Finding Corners..."
    for y in range(offset, height-offset):
        for x in range(offset, width-offset):
            #Calculate sum of squares
            windowIxx = Ixx[y-offset:y+offset+1, x-offset:x+offset+1]
            windowIxy = Ixy[y-offset:y+offset+1, x-offset:x+offset+1]
            windowIyy = Iyy[y-offset:y+offset+1, x-offset:x+offset+1]
            Sxx = windowIxx.sum()
            Sxy = windowIxy.sum()
            Syy = windowIyy.sum()

            #Find determinant and trace, use to get corner response
            det = (Sxx * Syy) - (Sxy**2)
            trace = Sxx + Syy
            r = det - k*(trace**2)

            #If corner response is over threshold, color the point and add to corner list
            if r > thresh:
                print x, y, r
                cornerList.append([x, y, r])
                color_img.itemset((y, x, 0), 0)
                color_img.itemset((y, x, 1), 0)
                color_img.itemset((y, x, 2), 255)
    return color_img, cornerList

def main():
    """
    Main parses argument list and runs findCorners() on the image
    :return: None
    """
    args, img_name = getopt.getopt(sys.argv[1:], '', ['window_size=', 'k_corner_response=', 'corner_threshold='])
    args = dict(args)
    print args
    window_size = args.get('--window_size')
    k = args.get('--k_corner_response')
    thresh = args.get('--corner_threshold')

    print("Image Name: " + str(img_name[0]))
    print("Window Size: " + str(window_size))
    print("K Corner Response: " + str(k))
    print("Corner Response Threshold:" + thresh)

    img = readImage(img_name[0])
    if img is not None:
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        if len(img.shape) == 4:
            img = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
        print "Shape: " + str(img.shape)
        print "Size: " + str(img.size)
        print "Type: " + str(img.dtype)
        print "Printing Original Image..."
        print(img)
        finalImg, cornerList = findCorners(img, int(window_size), float(k), int(thresh))
        if finalImg is not None:
            cv2.imwrite("finalimage.png", finalImg)

        # Write top 100 corners to file
        cornerList.sort(key=operator.itemgetter(2))
        outfile = open('corners.txt', 'w')
        for i in range(100):
            outfile.write(str(cornerList[i][0]) + ' ' + str(cornerList[i][1]) + ' ' + str(cornerList[i][2]) + '\n')
        outfile.close()


if __name__ == "__main__":
    main()