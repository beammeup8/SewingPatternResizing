#!/usr/bin/python 

import cv2 as cv
import numpy as np
import argparse
import random as rng

threshold = 100
min_bound_size = 100

def find_pieces(image_file):
    image = cv.imread(image_file)
    assert image is not None, "file could not be read, check with os.path.exists()"

    grey = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(grey, (5,5), 0)
    kernel = np.ones((10,10),np.uint8)
    morph = cv.morphologyEx(grey, cv.MORPH_GRADIENT, kernel)

    canny_output = cv.Canny(morph, threshold, threshold * 2)
    
    
    contours, _ = cv.findContours(canny_output, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    # Convert all the dashed lines in the pattern to solid lines 
    # so that the outermost one can be grabbed instead of 
    # whichever is a solid line

    
    # Find boundries
    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])

    # output the result 
    drawing = image.copy()

    boundries, final_contours = filter_bounds(boundRect, contours_poly)

    contour_color = (255,255,255,255)
    for i in range(len(final_contours)):
        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256), 255)
        cv.drawContours(drawing, final_contours, i, contour_color)
        bound = boundries[i]
        cv.rectangle(drawing, (int(bound[0]), int(bound[1])), \
          (int(bound[0]+bound[2]), int(bound[1]+bound[3])), color, 2)
    
    cv.imwrite('Contours.png', drawing)
    print(len(boundries))

def filter_bounds(boundRect, contours_poly):
    new_bounds = []
    new_conts = []
    for bound, cont in zip(boundRect, contours_poly):
        if bound[2] < min_bound_size or bound[3] < min_bound_size:
            continue

        new_bounds.append(bound)
        new_conts.append(cont)

    return new_bounds, new_conts

find_pieces('BodicePrincessSleeved_GH_A0_1105Upton.jpg')
