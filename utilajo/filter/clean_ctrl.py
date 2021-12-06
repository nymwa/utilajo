import sys
from argparse import ArgumentParser
from utilajo.util.template import make_main

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-r', '--reverse', dest = 'rev', action = 'store_true')
    return parser.parse_args()


def clean_ctrl(args):
    ctrl_list = [x for x in range(0x00, 0x20)]
    ctrl_list += [0x7f]
    ctrl_list += [x for x in range(0x80, 0xa0)]
    ctrl_list += [x for x in range(0x2400, 0x2427)]
    ctrl_list = [chr(x) for x in ctrl_list]
    ctrl_set = set(ctrl_list)

    for x in sys.stdin:
        x = x.strip()
        if (len(set(x) & ctrl_set) == 0) ^ args.rev:
            print(x)


main = make_main(clean_ctrl, parse_args = parse_args)

