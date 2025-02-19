import cv2
from blake3 import blake3
import random

# Inisuallze the camera and takes a photo
cam = cv2.VideoCapture(0)
if cam.grab():
    pic = cam.read()[1]

    # takes the bytes of the picure and and sets it to the hex of it
    seed = blake3(pic.tobytes()).hexdigest()

    # sets the seed to the one from blake3
    random.seed(seed) 

    # asks for a Minimum and Maximum Number
    print("Random number generator\n"+("-"*100))
    print(f"Seed: {seed}")
    min = int(input("Minimum Number: "))
    max = int(input("Maximum Number: "))

    # Prints a number between the range
    print(f"Random number: {random.randint(min,max)}")
else:
    # if there is no camera
    print("Camera is not open/available")