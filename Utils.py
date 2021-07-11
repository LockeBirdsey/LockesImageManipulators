def rgb_to_hex(red, green, blue):
    val = blue + (green * 256) + (red * 65536)
    return val


def decimal_colour_to_rgb(colour):
    red = int(colour / 65536)
    green = int(colour % 65536 / 256)
    blue = int(colour % 256)
    return red, green, blue