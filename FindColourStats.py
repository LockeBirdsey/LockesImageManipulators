from PIL import Image
from Utils import rgb_to_hex, decimal_colour_to_rgb

im = Image.open("C:/Users/lollb/Pictures/cc89170fde7eaede.jpeg")
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

# top 10 colours
print("top 10 colours:")
start = entries - 1
for i in range(10):
    colour = list(colour_counts_sorted_by_freq.keys())[start - i]
    colour_as_rgb = decimal_colour_to_rgb(colour)
    print("top " + str(i) + " is: " + str(colour_as_rgb) + " or " + str(hex(int(colour))) + " with " + str(
        colour_counts[colour]) + " occurrences")
