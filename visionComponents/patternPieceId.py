#!/usr/bin/python 

import cv2 as cv
import numpy as np
import random as rng

from outputOntoImage import output_boxes_on_image, output_contours_on_image

threshold = 200
min_bound_size = 100

def find_pieces_from_image_file(imageFile):
    image = cv.imread(imageFile)
    return find_pieces(image)

def find_pieces(image):
    assert image is not None, "image is not instantiated"

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

def get_bounded_areas(contours, boundRect, image):
    mask_color = (255, 255, 255)
    color = (0, 255, 0)
    blank_image = np.zeros(image.shape[:2], dtype=np.uint8)
    for i in range(len(contours)):
        x,y,w,h = boundRect[i]
        mask = blank_image.copy()
        cv.drawContours(mask, contours, i, mask_color, -1)
        masked = cv.bitwise_and(image, image, mask=mask)
        masked[mask==0] = mask_color
        cropped = masked[y:y+h, x:x+w]
        cv.imwrite("masked" + str(i) + ".png", cropped)
    

if __name__ == "__main__":
    image_file = 'testFiles/5oo4-Riptide-Reversible-Shorties-A0-Pattern-Pieces.png'
    image = cv.imread(image_file)
    boundRect, contours = find_pieces(image)
    import os
    path, fileName = os.path.split(image_file)
    output_boxes_on_image(image, boundRect, path + "/bounded_" + fileName)
    output_contours_on_image(image, contours, path + "/contours_" + fileName)

    get_bounded_areas(contours, boundRect, image)
