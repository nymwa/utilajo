import sys
from argparse import ArgumentParser
from utilajo.util.template import make_main

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('char_list', default = '')
    return parser.parse_args()


def senliterigi(args):
    for x in sys.stdin:
        x = x.strip()
        if all(char not in x for char in args.char_list):
            print(x)


main = make_main(senliterigi, parse_args)

