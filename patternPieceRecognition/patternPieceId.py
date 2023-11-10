#!/usr/bin/python 

import cv2 as cv
import numpy as np
import argparse
import random as rng

threshold = 100

def find_pieces(image_file):
    image = cv.imread(image_file)
    assert image is not None, "file could not be read, check with os.path.exists()"

    grey = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel = np.ones((10,10),np.uint8)
    morph = cv.morphologyEx(grey, cv.MORPH_GRADIENT, kernel)

    canny_output = cv.Canny(morph, threshold, threshold * 2)
    
    
    contours, _ = cv.findContours(canny_output, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    # Convert all the dashed lines in the pattern to solid lines 
    # so that the outermost one can be grabbed instead of 
    # whichever is a solid line

    
    # Find boundries
    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])
    
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    
    
    for i in range(len(contours)):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv.drawContours(drawing, contours_poly, i, color)
        cv.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
          (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)
    
    
    cv.imwrite('Contours.png', drawing)
    


find_pieces('BodicePrincessSleeved_GH_A0_1105Upton.jpg')
