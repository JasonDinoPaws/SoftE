import cv2
from blake3 import blake3
import random

# Inisuallze the camera and takes a photo
cam = cv2.VideoCapture(0)
if not cam.grab():
    raise ValueError("Camera Not open")
pic = cam.read()[1]

# takes the bytes of the picure and and sets it to the hex of it
seed = blake3(pic.tobytes()).hexdigest()

# sets the seed to the one from blake3
random.seed(seed) 

min = 1
max = int(input("Maximum Number: "))

def GetRanNum():
    return random.randint(min,max)