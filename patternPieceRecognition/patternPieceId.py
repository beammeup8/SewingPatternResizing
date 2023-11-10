#!/usr/bin/python 

import cv2 as cv
import numpy as np
import argparse
import random as rng

threshold = 100
min_bound_size = 100

def find_pieces(image):
    assert image is not None, "file could not be read, check with os.path.exists()"

    grey = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel = np.ones((10,10),np.uint8)

    #handles the dashed lines
    morph = cv.morphologyEx(grey, cv.MORPH_GRADIENT, kernel)
    canny_output = cv.Canny(morph, threshold, threshold * 2)
    contours, _ = cv.findContours(canny_output, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    # Find boundries
    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])

    return filter_bounds(boundRect, image.shape)

def filter_bounds(boundRect, image_shape):
    filled_image = np.zeros((image_shape[0], image_shape[1],3), np.uint8)
    color = (255, 255, 255)
    for bound in boundRect:
        x, y, w, h = bound
        if w < min_bound_size or h < min_bound_size:
            continue
        
        cv.rectangle(filled_image, (x, y), (x + w, y + h), color, -1)

    # It is only black and white, so really not sure why 
    # this is needed but it does not work if I remove it, 
    # so my best guess is that it has to do with the color channels?
    grey = cv.cvtColor(filled_image,cv.COLOR_BGR2GRAY)

    contours, _ = cv.findContours(grey, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    new_bounds = [None]*len(contours)
    for i, c in enumerate(contours):
        contour_poly = cv.approxPolyDP(c, 3, True)
        new_bounds[i] = cv.boundingRect(contour_poly)

    return new_bounds

def output_boxes_on_image(original_image, boundaries, new_file_name):
    drawing = original_image.copy()
    color = (0, 255, 0)
    for x, y, w, h in boundaries:
        cv.rectangle(drawing, (x, y), (x + w, y + h), color, 4)

    cv.imwrite(new_file_name, drawing)

if __name__ == "__main__":
    image_file = 'BodicePrincessSleeved_GH_A0_1105Upton.jpg'
    image = cv.imread(image_file)
    boundRect = find_pieces(image)
    output_boxes_on_image(image, boundRect, "bounded_" + image_file)


