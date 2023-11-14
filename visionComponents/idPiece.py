#!/usr/bin/python

import cv2 as cv
import pytesseract

# change this if you are not on linux
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
config = ('-l eng — oem 1 — psm 3')
          
def extract_text(piece):
  gray = cv.cvtColor(piece, cv.COLOR_BGR2GRAY)
  noise = cv.medianBlur(gray,3)
  thresh = cv.threshold(noise, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
  
  text = pytesseract.image_to_string(thresh, config=config)
  print(text)

if __name__ == "__main__":
  from getIndividualPieces import find_pieces_from_image_file
  filename = "testFiles/BodicePrincessSleeved_GH_A0_1105Upton.png"
  pieces = find_pieces_from_image_file(filename)
  print(len(pieces))
  for piece in pieces:
    extract_text(piece)