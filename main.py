#!/usr/bin/python 
import os

from pdfManagement.imageFromPDF import convert_to_image
from visionComponents.patternPieceId import find_pieces_from_image_file
from visionComponents.outputOntoImage import output_boxes_on_image, output_contours_on_image

def runProcessing(dirPath):
  files = filter(lambda x: x.endswith(".pdf"), os.listdir(dirPath))
  imageFiles = []
  for pdfFileName in files:
    imageFiles.extend(convert_to_image(dirPath + "/" + pdfFileName))
  
  print(imageFiles)
  for imageFile in imageFiles:
    boundRect, contrours = find_pieces_from_image_file(imageFile)
    

runProcessing("testFiles")