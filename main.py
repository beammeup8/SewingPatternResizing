#!/usr/bin/python 
import os

from pdfManagement.imageFromPDF import convert_to_image
from visionComponents.getIndividualPieces import find_pieces_from_image_file

def runProcessing(dirPath):
  files = filter(lambda x: x.endswith(".pdf"), os.listdir(dirPath))
  imageFiles = []
  for pdfFileName in files:
    imageFiles.extend(convert_to_image(dirPath + "/" + pdfFileName))
  
  print(imageFiles)
  for imageFile in imageFiles:
    pieces = find_pieces_from_image_file(imageFile)


runProcessing("testFiles")