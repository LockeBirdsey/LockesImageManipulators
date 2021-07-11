#!/usr/local/bin/python3
from PIL import Image


# stolen from https://stackoverflow.com/questions/47143332/how-to-pixelate-a-square-image-to-256-big-pixels-with-python
def pixelator(inpath, outpath, pixelsize=16, downsample=Image.BILINEAR, upsample=Image.NEAREST):
    img = Image.open(inpath)
    size = img.size
    x = pixelsize
    img_small = pixelator_down(img, x, downsample)
    result = pixelator_up(img_small, size, upsample)
    result.save(outpath)


def pixelator_down(img, pixelsize=16, downsample=Image.BILINEAR):
    x = pixelsize

    # Resize smoothly down to 16x16 pixels
    imgSmall = img.resize((x, x), resample=downsample)
    return imgSmall


def pixelator_up(img, origsize, upsample=Image.NEAREST):
    # Scale back up using NEAREST to original size
    result = img.resize(origsize, upsample)
    return result


if __name__ == '__main__':
    pixelator("C:/Users/lollb/Pictures/Esfjap0XUAAdIP0.jfif", "result_pixelator.png")
