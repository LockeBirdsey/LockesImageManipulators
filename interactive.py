from PIL import Image

import Averager
import MarkovChain

MARKOV_CHAIN = "MarkovChain"
AVERAGER = "Averager"
options = [MARKOV_CHAIN, AVERAGER]
quit_words = ["q", "Q", "quit", "Quit", "exit", "Exit"]
file_input_end = ["finish", "Finish"]
img_exts = ["ase", "art", "bmp", "blp", "cd5", "cit", "cpt", "cr2", "cut", "dds", "dib", "djvu", "egt", "exif", "gif",
            "gpl", "grf", "icns", "ico", "iff", "jng", "jpeg", "jpg", "jfif", "jp2", "jps", "lbm", "max", "miff", "mng",
            "msp", "nitf", "ota", "pbm", "pc1", "pc2", "pc3", "pcf", "pcx", "pdn", "pgm", "PI1", "PI2", "PI3", "pict",
            "pct", "pnm", "pns", "ppm", "psb", "psd", "pdd", "psp", "px", "pxm", "pxr", "qfx", "raw", "rle", "sct",
            "sgi", "rgb", "int", "bw", "tga", "tiff", "tif", "vtf", "xbm", "xcf", "xpm", "3dv", "amf", "ai", "awg",
            "cgm", "cdr", "cmx", "dxf", "e2d", "egt", "eps", "fs", "gbr", "odg", "svg", "stl", "vrml", "x3d", "sxd",
            "v2d", "vnd", "wmf", "emf", "art", "xar", "png", "webp", "jxr", "hdp", "wdp", "cur", "ecw", "iff", "lbm",
            "liff", "nrrd", "pam", "pcx", "pgf", "sgi", "rgb", "rgba", "bw", "int", "inta", "sid", "ras", "sun", "tga"]


def pretty(klist):
    return ' or '.join(klist)


def check_valid_image_file(file):
    file = str(file).lower()
    ending = file.split('.')[len(file.split('.')) - 1]
    return file not in quit_words and file not in file_input_end and ending in img_exts


def load_files_as_images(list_of_fnames):
    images = []
    for f in list_of_fnames:
        images.append(Image.open(f))
    return images


def main():
    res = ""
    exit_interactive = False
    while res not in quit_words:
        res = input("Select methods. Available methods are: {}. : ".format(pretty(options)))
        method = None
        if res not in options and res not in quit_words:
            print("Not a valid option")
        elif res in quit_words:
            break
        else:
            method = res

            file = ""
            file_list = []
            while file not in quit_words and file not in file_input_end:
                file = input("Type file paths. Type {} to stop: ".format(pretty(file_input_end)))
                if check_valid_image_file(file):
                    file_list.append(file)

            print("Files to import are:")
            print('\n'.join(file_list))

            print("Loading images....")
            images = load_files_as_images(file_list)
            print("Files loaded")

            # Ask for options
            output = None
            if method == MARKOV_CHAIN:
                bucket_size = int(input("Enter MarkovChain bucket size [n > 0](preferred: 16): ").strip())
                four_neighbours = bool(input(
                    "Enter if four or eight neighbours should be used [True|False](True is 4 Neighbours): ").strip())
                chain = MarkovChain.MarkovChain(bucket_size=bucket_size, four_neighbour=four_neighbours)
                for img in images:
                    chain.train(img)
                output = chain.generate()
            elif method == AVERAGER:
                noise = bool(input("Enter if a noise layer is desired[True|False] : ").strip())
                avg = Averager.ImageAverager()
                output = avg.averager(list_of_img_data=images, add_noise=noise)

            out_name = input("Enter desired output name: ").strip()
            output.save(out_name)
            print("Finished running {}".format(method))


if __name__ == "__main__":
    main()
