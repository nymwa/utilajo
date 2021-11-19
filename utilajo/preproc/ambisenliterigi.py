import sys
from argparse import ArgumentParser
from utilajo.util.template import make_main

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('char_list', default = '')
    return parser.parse_args()


def ambisenliterigi(args):
    for x in sys.stdin:
        src, trg = x.strip().split('\t')
        if all((char not in src) and (char not in trg) for char in args.char_list):
            print('{}\t{}'.format(src, trg))


main = make_main(ambisenliterigi, parse_args)

