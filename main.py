import os
import re
import tempfile

import cv2
import numpy as np
import pytesseract
from PIL import Image

filename = 'images/file-1.jpg'

def ocr_core(filename):
    return pytesseract.image_to_string(filename)

def get_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    return cv2.medianBlur(image, 5)

def thresholding(image):
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

img = cv2.imread(filename)
img = get_grayscale(img)
img = remove_noise(img)
img = thresholding(img)

# Create a temporary file to save the processed image
temp_image_path = os.path.join(tempfile.gettempdir(), "processed_image.jpg")
cv2.imwrite(temp_image_path, img)

# Perform OCR on the temporary processed image
result = ocr_core(temp_image_path)

# Remove the temporary file
os.remove(temp_image_path)


def extractNumber(text):
    # Define a regular expression pattern to match credit card numbers
    text_pattern = r"(GHA-\d*-\d)"

    # Find all occurrences of credit card numbers in the response
    print(text)
    print(re.findall(text_pattern, text))


custom_config = '--oem 3 --psm 6'
reader = pytesseract.image_to_string(filename, config=custom_config)
extractNumber(reader)