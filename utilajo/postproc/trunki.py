import sys
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-n', type = int)
    parser.add_argument('-m', type = int, default = 1)
    parser.add_argument('-i', '--inverse', action = 'store_true')
    parser.add_argument('-r', '--reflect', action = 'store_true')
    parser.add_argument('-s', '--source')
    parser.add_argument('-t', '--target')
    parser.add_argument('-w', '--write-index', action = 'store_true')
    parser.add_argument('-x', '--index-in')
    parser.add_argument('-y', '--index-out')
    return parser.parse_args()


def normal(n, m, inverse):
    for line in sys.stdin:
        line = line.strip()
        length = len(line.split())
        if (m <= length <= n) ^ inverse:
            print(line)


def reflect(n, m, inverse, src, trg):
    with open(src) as f, open(trg, 'w') as g:
        for line, orig in zip(sys.stdin, f):
            line = line.strip()
            orig = orig.strip()
            length = len(line.split())
            if (m <= length <= n) ^ inverse:
                print(line)
                print(orig, file = g)


def write_indices(n, m, inverse, index_out):
    with open(index_out, 'w') as f:
        for line in sys.stdin:
            line = line.strip()
            length = len(line.split())
            if (m <= length <= n) ^ inverse:
                print(line)
                print('o', file = f)
            else:
                print('x', file = f)


def main():
    args = parse_args()

    if args.reflect:
        reflect(args.n, args.m, args.inverse, args.source, args.target)
    elif args.write_index:
        write_indices(args.n, args.m, args.inverse, args.index_out)
    else:
        normal(args.n, args.m, args.inverse)


