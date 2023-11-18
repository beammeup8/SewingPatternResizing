#!/usr/bin/python

import cv2 as cv
import easyocr as ocr
          
def extract_text(pieceFileName):
  reader = ocr.Reader(['en'], gpu = True)
  text = reader.readtext(pieceFileName)
  # lines = [l for l in text.split("\n", maxsplit=0) if l.strip() != ""]
  # return '\n'.join(lines)
  return text

if __name__ == "__main__":
  from getIndividualPieces import find_pieces_from_image_file
  filename = "testFiles/BodicePrincessSleeved_GH_A0_1105Upton.png"
  pieces = find_pieces_from_image_file(filename)
  print(len(pieces))
  cnt = 0
  for image in pieces:
    filename = "testFiles/piece_" + str(cnt) + ".png"
    cv.imwrite(filename, image)
    text = extract_text(filename)
    f = open("testFiles/piece_" + str(cnt) + ".txt", "w")
    f.write(str(text))
    cnt += 1