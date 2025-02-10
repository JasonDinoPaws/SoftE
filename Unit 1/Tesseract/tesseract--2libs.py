# Imports
import cv2 # Opening file, cropping and converting to gray
from os import listdir,system,remove # get files from a dir

file = open("outfile.txt","w") # output file
folder = "tess-Input" # folder path

# Adding and checking a image
def addtext(fi):
    # Reads the image and crops it to the point, then creates another var to make it gray
    img = cv2.imread(f"{folder}/{fi}")[15:15+49,27:372]
    imgg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Reads both the image with color and the image that is gray and strips them of any whitespace and \n
    img = cv2.imwrite("img.png",img)
    imgg = cv2.imwrite("imgg.png",imgg)
    system("tesseract img.png out")
    system("tesseract imgg.png outg")

    with open("out.txt") as out: text = out.read().strip()
    with open("outg.txt") as outg: textg = outg.read().strip()

    if len(text) > 0:
        file.write(text)
    elif len(textg) > 0:
        file.write(textg)
    else:
        file.write(f"Failed to get Text from {fi}")
    file.write("\n")

for fi in listdir(folder):
    addtext(fi)


remove("out.txt")
remove("outg.txt")
remove("img.png")
remove("imgg.png")
file.close()