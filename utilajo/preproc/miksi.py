import sys
import random as rd
from argparse import ArgumentParser
from utilajo.util.template import make_main

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-s', '--seed', type = int, default = None)
    return parser.parse_args()


def miksi(args):
    xs = [x.rstrip('\n') for x in sys.stdin]

    if args.seed is not None:
        rd.seed(args.seed)
    rd.shuffle(xs)

    for x in xs:
        print(x)


main = make_main(miksi, parse_args = parse_args)

