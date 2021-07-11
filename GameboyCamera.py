from PIL import Image
import numpy as np

# nicked from https://github.com/iechevarria/gameboy-camera-filter
from Pixelator import pixelator_down, pixelator_up


def gbc_full(path):
    img = Image.open(path).convert('L')
    size = img.size
    s1 = pixelator_down(img, 128, Image.BILINEAR)
    s2 = gbc(s1)
    s3 = pixelator_up(s2, size)
    s3.save("result_pixel_gbc_filter.png")
    return s3


def gbc_main(filename):
    img = Image.open(filename).convert('L')
    img = gbc(img)
    filename = filename.split(".")[0] + "_gbc_filter.png"
    img.save(filename)
    print("Saved to " + filename)


def gbc(img):
    img = np.asarray(img)
    img.flags.writeable = True
    img = gbc_filter(img)
    img = Image.fromarray(img, 'L')
    return img


def gbc_filter(img):
    """Applies Game Boy camera filter"""
    for i in range(int(img.shape[0])):
        for j in range(int(img.shape[1])):
            if img[i][j] >= 236:
                img[i][j] = 255
            elif img[i][j] >= 216:
                img[i][j] = 255 - ((i % 2) * (j % 2) * 83)
            elif img[i][j] >= 196:
                img[i][j] = 255 - (((j + i + 1) % 2) * 83)
            elif img[i][j] >= 176:
                img[i][j] = 172 + (((i + 1) % 2) * (j % 2) * 83)
            elif img[i][j] >= 157:
                img[i][j] = 172
            elif img[i][j] >= 137:
                img[i][j] = 172 - ((i % 2) * (j % 2) * 86)
            elif img[i][j] >= 117:
                img[i][j] = 172 - (((j + i + 1) % 2) * 86)
            elif img[i][j] >= 97:
                img[i][j] = 86 + (((i + 1) % 2) * (j % 2) * 86)
            elif img[i][j] >= 78:
                img[i][j] = 86
            elif img[i][j] >= 58:
                img[i][j] = 86 - ((i % 2) * (j % 2) * 86)
            elif img[i][j] >= 38:
                img[i][j] = 86 - (((j + i + 1) % 2) * 86)
            elif img[i][j] >= 18:
                img[i][j] = 0 + (((i + 1) % 2) * (j % 2) * 86)
            else:
                img[i][j] = 0
    return img


if __name__ == '__main__':
    gbc_full("C:/Users/lollb/Pictures/75349224_460503281489895_6964218294265970688_n.jpg")
    # gbc_main("C:/Users/lollb/Pictures/Esfjap0XUAAdIP0.jfif")
