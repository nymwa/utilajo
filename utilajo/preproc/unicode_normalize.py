import sys
import unicodedata
from argparse import ArgumentParser
from utilajo.util.template import make_main

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-f', '--form', default = 'NFKC')
    return parser.parse_args()


def normalize(args):
    for x in sys.stdin:
        x = x.strip()
        x = unicodedata.normalize(args.form, x)
        print(x)


main = make_main(normalize, parse_args = parse_args)

