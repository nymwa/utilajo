import sys
from argparse import ArgumentParser
from utilajo.util.template import make_main

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-t', type=float, default = 2.0)
    parser.add_argument('-r', action = 'store_true')
    return parser.parse_args()


def preproc(th, rev = False):
    for x in sys.stdin:
        x = x.strip()
        src, trg = x.split('\t')
        src_len = len(src.split())
        trg_len = len(trg.split())
        if rev ^ ((src_len <= trg_len * th) and (trg_len <= src_len * th)):
            print(x)


main = make_main(
        lambda args: preproc(th = args.t, rev = args.r),
        parse_args = parse_args)

