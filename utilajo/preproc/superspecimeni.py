from argparse import ArgumentParser
from contextlib import ExitStack

def oversample(src_in, trg_in, src_out, trg_out, i, o):
    for src, trg in zip(src_in, trg_in):
        if src == trg:
            n = i
        else:
            n = o
        for _ in range(n):
            print(src.strip(), file = src_out)
            print(trg.strip(), file = trg_out)


def oversample_with_edit_dist(src_in, trg_in, src_out, trg_out):
    assert False # YET NOT IMPLEMENTED


def enter(stack, path, mode = 'r'):
    return stack.enter_context(open(path, mode = mode))


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('source_input_path')
    parser.add_argument('target_input_path')
    parser.add_argument('source_output_path')
    parser.add_argument('target_output_path')
    parser.add_argument('-i', type = int, default = 1, help = 'identical input and output')
    parser.add_argument('-o', type = int, default = 1, help = 'oversampling different input and output')
    parser.add_argument('--edit-dist', action = 'store_true')
    return parser.parse_args()


def main():
    args = parse_args()

    with ExitStack() as stack:
        src_in = enter(stack, args.source_input_path)
        trg_in = enter(stack, args.target_input_path)
        src_out = enter(stack, args.source_output_path, mode = 'w')
        trg_out = enter(stack, args.target_output_path, mode = 'w')
        if args.edit_dist:
            oversample_with_edit_dist(src_in, trg_in, src_out, trg_out, args.i, args.o)
        else:
            oversample(src_in, trg_in, src_out, trg_out, args.i, args.o)

