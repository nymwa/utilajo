import sys
from argparse import ArgumentParser
from utilajo.util.template import make_main

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-r', '--reverse', dest = 'rev', action = 'store_true')
    return parser.parse_args()


def punct_end(args):
    punct_set = {'.', '!', '?', '"', "'", '”'}

    for x in sys.stdin:
        x = x.strip()
        if (x[-1] in punct_set) ^ args.rev:
            print(x)


main = make_main(punct_end, parse_args = parse_args)

