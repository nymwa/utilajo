import sys
import json
from argparse import ArgumentParser
import numpy as np
from collections import deque

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('langs', nargs = '+')
    parser.add_argument('-p', default = None)
    parser.add_argument('--buffer-size', default = None, type = int)
    return parser.parse_args()


class Sampler:

    def __init__(self, cands, p = None, buffer_size = None):

        self.cands = cands
        self.p = p

        self.queue = deque()

        if buffer_size is not None:
            self.buffer_size = buffer_size
        else:
            self.buffer_size = 10000

    def sampler(self):
        return np.random.choice(
                self.cands,
                size = self.buffer_size,
                p = self.p)

    def __call__(self):
        if not self.queue:
            self.queue.extend(self.sampler())
        return self.queue.pop()


def run_main(langs, p = None, buffer_size = None):
    sampler = Sampler(langs, p = p, buffer_size = buffer_size)

    for line in sys.stdin:
        x = json.loads(line.strip())
        lang = sampler()
        source = x[lang]
        target = x['trg']

        if (source is not None) and (target is not None):
            out = '{}\t{}'.format(source, target)
            print(out)


def main():
    args = parse_args()

    try:
        if args.p is not None:
            p = [float(x) for x in args.p.split(':')]
        else:
            p = None
        run_main(args.langs, p = p, buffer_size = args.buffer_size)
    except KeyboardInterrupt:
        pass
    except BrokenPipeError:
        pass


