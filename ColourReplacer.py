from PIL import Image

from Utils import rgb_to_hex, decimal_colour_to_rgb


class ReplaceRange:
    source_start, source_end = 0, 0
    replace_start, replace_end = 0, 0

    def __init__(self, inputstr):
        spl = inputstr.split("-")
        self.source_start = int(spl[0], 16)
        self.replace_start = int(spl[1], 16)
        print("source " + str(self.source_start))
        print("replace " + str(self.replace_start))

    def is_in(self, value_input):
        return self.source_start == value_input

    def convert(self, value_input):
        if self.source_start == value_input:
            return self.replace_start
        else:
            return value_input


im = Image.open("C:/Users/lollb/Pictures/cc89170fde7eaede.jpeg")
width, height = im.size
new_image = Image.new('RGB', (width, height))
new_data = new_image.load()

range_string = "fdfdfd-00FF00"
rs = ReplaceRange(range_string)
ranges = [rs, ReplaceRange("020202-00FF00"), ReplaceRange("b4d292-00FF00")]

changes = 0
for i in range(width):
    for j in range(height):
        pixVal = im.getpixel((i, j))
        fullPixVal = rgb_to_hex(pixVal[0], pixVal[1], pixVal[2])
        for r in ranges:
            new_data[(i, j)] = decimal_colour_to_rgb(r.convert(fullPixVal))
            if r.is_in(fullPixVal):
                changes += 1
                # print("new value" + str(decimal_colour_to_rgb(r.convert(fullPixVal))))

print(width * height)
print("changes: " + str(changes))
print("percentage changed: " + str(changes / (width * height) * 100))
new_image.save("combined_test.png", "png")
