# Imports
from PIL import Image # litterly just need it for tesseract
import pytesseract # Tesseract
import cv2 # Opening file, cropping and converting to gray
from os import listdir # get files from a dir

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract' # sets the tesseract to the bin file
file = open("outfile.txt","w") # output file
folder = "tess-Input" # folder path

# Adding and checking a image
def addtext(fi):
    # Reads the image and crops it to the point, then creates another var to make it gray
    img = cv2.imread(f"{folder}/{fi}")[15:15+49,27:372]
    imgg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Reads both the image with color and the image that is gray and strips them of any whitespace and \n
    text = pytesseract.image_to_string(Image.fromarray(img)).strip()
    textg = pytesseract.image_to_string(Image.fromarray(imgg)).strip()

    if len(text) > 0:
        file.write(text)
    elif len(textg) > 0:
        file.write(textg)
    else:
        file.write(f"Failed to get Text from {fi}")
    file.write("\n")

for fi in listdir(folder):
    addtext(fi)

file.close()