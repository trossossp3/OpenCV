import cv2
import sys
import pytesseract
import numpy as np
 
#if __name__ == '__main__':
 

   
  # Read image path from command line
imPath = 'plate1.jpg'
     
  # Uncomment the line below to provide path to tesseract manually
  # pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
 
  # Define config parameters.
  # '-l eng'  for using the English language
  # '--oem 1' for using LSTM OCR Engine
config1 = ('--l eng')
 
  # Read image from disk
im = cv2.imread(imPath, cv2.IMREAD_COLOR)


 
  # Run tesseract OCR on image
text = pytesseract.image_to_string(im)
 
  # Print recognized text
print(text)
