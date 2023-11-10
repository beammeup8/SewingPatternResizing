#!/usr/bin/python 

import cv2 as cv
import numpy as np
import argparse
import random as rng

threshold = 200
min_bound_size = 100

def find_pieces(image):
    assert image is not None, "file could not be read, check with os.path.exists()"

    grey = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    kernel = np.ones((10,10),np.uint8)

    #handles the dashed lines
    canny_output = cv.Canny(grey, threshold, threshold * 2)
    morph = cv.morphologyEx(canny_output, cv.MORPH_GRADIENT, kernel)
    cv.imwrite("threshold.png", morph)
    contours, _ = cv.findContours(morph, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    
    # Find boundries
    contours_poly = [None]*len(contours)
    boundRect = [None]*len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.boundingRect(contours_poly[i])

    return boundRect, contours_poly

def output_boxes_on_image(original_image, boundaries, new_file_name):
    drawing = original_image.copy()
    color = (0, 255, 0)
    for x, y, w, h in boundaries:
        cv.rectangle(drawing, (x, y), (x + w, y + h), color, 4)

    cv.imwrite(new_file_name, drawing)

def output_contours_on_image(original_image, contours, new_file_name):
    drawing = original_image.copy()
    color = (0, 255, 0)
    cv.drawContours(drawing, contrours, -1, color, 2)
    cv.imwrite(new_file_name, drawing)

if __name__ == "__main__":
    image_file = 'BodicePrincessSleeved_GH_A0_1105Upton.jpg'
    image = cv.imread(image_file)
    boundRect, contrours = find_pieces(image)
    output_boxes_on_image(image, boundRect, "bounded_" + image_file)
    output_contours_on_image(image, contrours, "contours_" + image_file)


