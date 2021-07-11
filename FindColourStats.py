from PIL import Image
from Utils import rgb_to_hex, decimal_colour_to_rgb

im = Image.open("C:/Users/lollb/Pictures/Esfjap0XUAAdIP0.jfif")
width, height = im.size
mean = 0
colour_counts = dict()


def flatten_to_list(mydict):
    new_list = []
    for k, v in mydict.items():
        for _ in range(v):
            new_list.append(k)
    return sorted(new_list)


for i in range(width):
    for j in range(height):
        pixVal = im.getpixel((i, j))
        as_dec = rgb_to_hex(pixVal[0], pixVal[1], pixVal[2])
        if not colour_counts.__contains__(as_dec):
            colour_counts[as_dec] = 0
        colour_counts[as_dec] = colour_counts[as_dec] + 1
        mean += as_dec

# build colour squares
colour_squares = Image.new('RGB', (300, 400))
new_data = colour_squares.load()


def write_colour_square(img, x, y, color):
    for i in range(x, x + 100):
        for j in range(y, y + 100):
            img[(i, j)] = color


# mean
mean = mean / (width * height)
mean_as_rgb = decimal_colour_to_rgb(mean)
print("mean colour is: " + str(mean_as_rgb) + " or " + str(hex(int(mean))))

# median
sorted_flattened_list = flatten_to_list(colour_counts)
num_elements = len(sorted_flattened_list)
median = 0
if num_elements % 2 == 0:
    a = sorted_flattened_list[int(num_elements / 2)]
    b = sorted_flattened_list[int(num_elements / 2) + 1]
    median = int((a + b) / 2)
else:
    median = sorted_flattened_list[int(num_elements / 2)]

median_as_rgb = decimal_colour_to_rgb(median)
print("median colour is: " + str(median_as_rgb) + " or " + str(hex(int(median))))

# mode
colour_counts_sorted_by_freq = {k: v for k, v in sorted(colour_counts.items(), key=lambda item: item[1])}
# print(colour_counts_sorted_by_freq)
entries = len(colour_counts_sorted_by_freq.keys())
mode = list(colour_counts_sorted_by_freq.keys())[entries - 1]

mode_as_rgb = decimal_colour_to_rgb(mode)
print("mode colour is: " + str(mode_as_rgb) + " or " + str(hex(int(mode))))

# top 2-10 (1-9 from 0) colours
print("top 10 colours:")
start = entries - 1
x_off = 0
y_off = 100
for i in range(1, 10):
    colour = list(colour_counts_sorted_by_freq.keys())[start - i]
    colour_as_rgb = decimal_colour_to_rgb(colour)
    write_colour_square(new_data, x_off, y_off, colour_as_rgb)
    if x_off < 200:
        x_off += 100
    elif x_off == 200:
        x_off = 0
        y_off += 100
    print("top " + str(i) + " is: " + str(colour_as_rgb) + " or " + str(hex(int(colour))) + " with " + str(
        colour_counts[colour]) + " occurrences")

write_colour_square(new_data, 0, 0, mean_as_rgb)
write_colour_square(new_data, 100, 0, median_as_rgb)
write_colour_square(new_data, 200, 0, mode_as_rgb)
colour_squares.save("colour_squares.png", "png")
