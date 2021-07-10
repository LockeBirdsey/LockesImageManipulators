#!/usr/local/bin/python3
from PIL import Image

# stolen from https://stackoverflow.com/questions/47143332/how-to-pixelate-a-square-image-to-256-big-pixels-with-python

img = Image.open("C:/Users/lollb/Pictures/Esfjap0XUAAdIP0.jfif")
x = 64

# Resize smoothly down to 16x16 pixels
imgSmall = img.resize((x, x), resample=Image.NONE)

# Scale back up using NEAREST to original size
result = imgSmall.resize(img.size, Image.NEAREST)

# Save
result.save('result.png')
