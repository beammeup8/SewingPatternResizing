#!/usr/bin/python 

import cv2 as cv

image = cv.imread('BodicePrincessSleeved_GH_A0_1105Upton.jpg')
assert image is not None, "file could not be read, check with os.path.exists()"

gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

cv.imwrite("thresh.png", thresh)
