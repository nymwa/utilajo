import sys
from argparse import ArgumentParser

def load_valid_test_set(args):
    lst = []

    with open(args.valid) as f:
        for x in f:
            lst.append(x.rstrip('\n'))

    with open(args.test) as f:
        for x in f:
            lst.append(x.rstrip('\n'))

    return set(lst)


def main():
    parser = ArgumentParser()
    parser.add_argument('valid')
    parser.add_argument('test')
    args = parser.parse_args()

    valtest = load_valid_test_set(args)

    for line in sys.stdin:
        src, trg = line.rstrip('\n').split('\t')
        if trg not in valtest:
            print(src + '\t' + trg)

