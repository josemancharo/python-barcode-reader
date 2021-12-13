#!/usr/env/python3

from pyzbar import pyzbar
import cv2
import sys

def decode(image):
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        print("Type:", obj.type)
        print("Data:", obj.data)
        print()

    return image


path = sys.argv[1]
img = cv2.imread(path)
decode(img)