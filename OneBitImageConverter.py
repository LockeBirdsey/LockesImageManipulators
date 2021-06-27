from PIL import Image

im = Image.open("C:/Users/lollb/Pictures/cc89170fde7eaede.jpeg")
width, height = im.size
new_image = Image.new('RGB', (width, height))
data = new_image.load()

cutoff = 127

for i in range(width):
    for j in range(height):
        pixVal = im.getpixel((i, j))
        avg = (pixVal[0] + pixVal[1] + pixVal[2]) / 3
        value = 0
        if avg > cutoff:
            value = 255
        data[(i, j)] = (value, value, value)

new_image.save("test.png", "png")
