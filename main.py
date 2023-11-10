#!/usr/bin/python 
import os

from pdfManagement.imageFromPDF import convert_to_image

def runProcessing(dirPath):
  files = filter(lambda x: x.endswith(".pdf"), os.listdir(dirPath))
  imageFiles = []
  for pdfFileName in files:
    imageFiles.extend(convert_to_image(dirPath + "/" + pdfFileName))
  
  print(imageFiles)

runProcessing("testFiles")