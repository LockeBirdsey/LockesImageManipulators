from linedraw import linedraw
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM

outpath_svg = "ew.svg"
outpath_png = "ew.png"
linedraw.export_path = outpath_svg
lines = linedraw.sketch("C:/Users/lollb/Pictures/188671.jpg")  # return list of polylines, eg.

# not working, unsure why
# drawing = svg2rlg(outpath_svg)
# renderPM.drawToFile(drawing, outpath_png, fmt="PNG")

# [[(x,y),(x,y),(x,y)],[(x,y),(x,y),...],...]

# linedraw.visualize(lines)  # simulates plotter behavior
# # draw the lines in order using turtle graphics.
