from linedraw import linedraw

linedraw.export_path = "ew.png"
lines = linedraw.sketch("/Users/locke/Pictures/vlcsnap-2019-11-17-22h51m23s980.png")  # return list of polylines, eg.
# [[(x,y),(x,y),(x,y)],[(x,y),(x,y),...],...]

# linedraw.visualize(lines)  # simulates plotter behavior
# # draw the lines in order using turtle graphics.