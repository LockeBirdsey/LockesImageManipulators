from PIL import Image

im = Image.open("C:/Users/lollb/Pictures/red.png")
width, height = im.size
red_image = Image.new('RGB', (width, height))
green_image = Image.new('RGB', (width, height))
blue_image = Image.new('RGB', (width, height))
red_data = red_image.load()
green_data = green_image.load()
blue_data = blue_image.load()


for i in range(width):
    for j in range(height):
        pixVal = im.getpixel((i, j))
        red_data[(i, j)] = (pixVal[0], 0, 0)
        green_data[(i, j)] = (0, pixVal[1], 0)
        blue_data[(i, j)] = (0, 0, pixVal[2])

red_image.save("red_test.png", "png")
green_image.save("green_test.png", "png")
blue_image.save("blue_test.png", "png")
