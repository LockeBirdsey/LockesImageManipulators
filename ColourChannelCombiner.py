from PIL import Image

red_im = Image.open("C:/Users/lollb/repos/ImageManipulators/red_test.png")
blue_im = Image.open("C:/Users/lollb/repos/ImageManipulators/blue_test.png")
green_im = Image.open("C:/Users/lollb/repos/ImageManipulators/green_test.png")
width, height = red_im.size
new_image = Image.new('RGB', (width, height))
new_data = new_image.load()

for i in range(width):
    for j in range(height):
        rpixVal = red_im.getpixel((i, j))
        bpixVal = blue_im.getpixel((i, j))
        gpixVal = green_im.getpixel((i, j))
        new_data[(i, j)] = (rpixVal[0], gpixVal[1], bpixVal[2])

new_image.save("combined_test.png", "png")
