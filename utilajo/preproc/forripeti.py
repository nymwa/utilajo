import re
import sys
from argparse import ArgumentParser
from utilajo.util.template import make_main

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-r', '--rev', action = 'store_true')
    parser.add_argument('-a', '--n1', type=int, default = 5)
    parser.add_argument('-b', '--n2', type=int, default = 4)
    parser.add_argument('-c', '--n3', type=int, default = 4)
    parser.add_argument('-d', '--n4', type=int, default = 4)
    parser.add_argument('-e', '--n5', type=int, default = 3)
    parser.add_argument('-v', '--n6', type=int, default = 3)
    parser.add_argument('-w', '--n7', type=int, default = 3)
    parser.add_argument('-x', '--n8', type=int, default = 2)
    parser.add_argument('-y', '--n9', type=int, default = 2)
    parser.add_argument('-z', '--n10', type=int, default = 2)
    return parser.parse_args()

pattern_1 = re.compile(r'(.)(?=\1{4,})')

def forripeti(args):
    pattern_1 = re.compile(r'(.)(?=\1{' + str(args.n1 - 1) + ',})')
    pattern_2 = re.compile(r'(..)(?=\1{' + str(args.n2 - 1) + ',})')
    pattern_3 = re.compile(r'(...)(?=\1{' + str(args.n3 - 1) + ',})')
    pattern_4 = re.compile(r'(....)(?=\1{' + str(args.n4 - 1) + ',})')
    pattern_5 = re.compile(r'(.....)(?=\1{' + str(args.n5 - 1) + ',})')
    pattern_6 = re.compile(r'(......)(?=\1{' + str(args.n6 - 1) + ',})')
    pattern_7 = re.compile(r'(.......)(?=\1{' + str(args.n7 - 1) + ',})')
    pattern_8 = re.compile(r'(........)(?=\1{' + str(args.n8 - 1) + ',})')
    pattern_9 = re.compile(r'(.........)(?=\1{' + str(args.n9 - 1) + ',})')
    pattern_10 = re.compile(r'(..........+)(?=\1{' + str(args.n10 - 1) + ',})')

    for x in sys.stdin:
        x = x.strip()
        if args.rev ^ (not
                (pattern_1.search(x)
                or pattern_2.search(x)
                or pattern_3.search(x)
                or pattern_4.search(x)
                or pattern_5.search(x)
                or pattern_6.search(x)
                or pattern_7.search(x)
                or pattern_8.search(x)
                or pattern_9.search(x)
                or pattern_10.search(x))):
            print(x)


main = make_main(forripeti, parse_args = parse_args)

