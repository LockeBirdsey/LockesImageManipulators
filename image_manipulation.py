import argparse
import distutils.util
import random

from PIL import Image

import Averager
import MarkovChain

MARKOV_CHAIN = "MarkovChain"
AVERAGER = "Averager"
methods = [MARKOV_CHAIN, AVERAGER]


def process_args(arguments):
    arg_dict = {}
    if args is None:
        return arg_dict
    else:
        for a in arguments:
            spl = a.split('=')
            arg_dict.update({spl[0]: spl[1]})
        return arg_dict


def load_files_as_images(list_of_fnames):
    images = []
    for f in list_of_fnames:
        images.append(Image.open(f))
    return images


def pretty_dict(arguments):
    out = []
    for i in arguments.items():
        out.append(str(i[0]) + "=" + str(i[1]))
    out_str = '-'.join(out)
    out_str = "(" + out_str + ")"
    return out_str


parser = argparse.ArgumentParser(description="Do some image manipulation.")
parser.add_argument('--files', type=str, nargs='*', help="a list of files to be processed. ")
parser.add_argument('--method', type=str, help="Available methods", choices=methods)
parser.add_argument('--args', type=str, nargs='*', help="Method arguments.")
parser.add_argument('--output', type=str, help="File output")
parser.add_argument('--print-method-args', type=str, choices=methods,
                    help="Prints the argument details for a method")
args = parser.parse_args()

if args.print_method_args:
    print(args.print_method_args + " arguments are:")
    if args.print_method_args == MARKOV_CHAIN:
        print("\tBUCKET_SIZE: The size of the colour bucket. Number between 0 and 255. Default is 16")
        print(
            "\tFOUR_NEIGHBOURS: Whether four neighbours should be used. True for four, False for eight. Default is True")
        print("\tDISPLAY_PROGRESS: Whether progress should be visualised. Accepts True or False. Default is False")
    elif args.print_method_args == AVERAGER:
        print("\tADD_NOISE: Whether a noise layer should be added. Accepts True or False. Default is False")

if args.method:
    proc_args = process_args(args.args)
    images = load_files_as_images(args.files)
    output = None
    values = {}
    if args.method == MARKOV_CHAIN:
        values = {"BUCKET_SIZE": 16, "FOUR_NEIGHBOURS": True, "DISPLAY_PROGRESS": False}
        values.update(proc_args)
        print("Using " + args.method + " with arguments: " + str(values))
        bucket_size = int(values["BUCKET_SIZE"])
        four_neighbours = bool(distutils.util.strtobool(values["FOUR_NEIGHBOURS"]))
        display_progress = bool(distutils.util.strtobool(values["DISPLAY_PROGRESS"]))
        chain = MarkovChain.MarkovChain(bucket_size=bucket_size, four_neighbour=four_neighbours,
                                        display_progress=display_progress)
        for img in images:
            chain.train(img)
        output = chain.generate()
    elif args.method == AVERAGER:
        values = {"ADD_NOISE": False}
        values.update(proc_args)
        noise = bool(distutils.util.strtobool(values["ADD_NOISE"]))
        print("Using " + args.method + " with arguments: " + str(values))
        avg = Averager.ImageAverager()
        output = avg.averager(list_of_img_data=images, add_noise=noise)
    if args.output:
        output.save(args.output)
    else:
        save_dest = args.method + "-" + pretty_dict(values) + "-" + str(
            random.randint(0, 100000)) + ".png"
        print("No output name provided. Saving to " + save_dest)
        output.save(save_dest)
