import cv2
from blake3 import blake3
import random


cam = cv2.VideoCapture(0)
if cam.grab():
    pic = cam.read()[1]

    seed = blake3(pic.tobytes()).hexdigest()

    random.seed(seed)

    print("Random number generator\n"+("-"*100))
    print(f"Seed: {seed}")
    min = int(input("Minimum Number: "))
    max = int(input("Maximum Number: "))

    print(f"Random number: {random.randint(min,max)}")
else:
    print("Camera is not open/available")