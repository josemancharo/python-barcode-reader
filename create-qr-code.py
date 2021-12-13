#!/usr/env/python3
import qrcode
import sys

input_data = sys.argv[1]
output_file = sys.argv[2]

img = qrcode.make(input_data)
img.save(output_file)
