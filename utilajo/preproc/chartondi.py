import sys
from argparse import ArgumentParser
from utilajo.util.template import make_main

def get_length(line):
    return len(line.strip())


def cond(args, x):
    length = get_length(x)
    return args.min_len <= length <= args.max_len


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--min-len', type=int, default = 1)
    parser.add_argument('--max-len', type=int, default = 500)
    return parser.parse_args()


def tondi(args):
    for x in sys.stdin:
        x = x.strip()
        if cond(args, x):
            print(x)


main = make_main(tondi, parse_args = parse_args)

