import sys
from argparse import ArgumentParser
from utilajo.util.template import make_main

def get_length(line):
    return len(line.strip().split())


def cond(args, src, trg):
    src_length = get_length(src)
    if not (args.min_len <= src_length <= args.max_len):
        return False

    trg_length = get_length(trg)
    if not (args.min_len <= trg_length <= args.max_len):
        return False

    return True


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--min-len', type=int, default = 1)
    parser.add_argument('--max-len', type=int, default = 400)
    return parser.parse_args()


def ambitondi(args):
    for line in sys.stdin:
        line = line.rstrip('\n')
        src, trg = line.split('\t')
        if cond(args, src, trg):
            line = '{}\t{}'.format(src, trg)
            print(line)


main = make_main(ambitondi, parse_args = parse_args)

