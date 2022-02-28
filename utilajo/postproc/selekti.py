import sys
import json
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('lang')
    return parser.parse_args()


def run_main(lang):
    for line in sys.stdin:
        x = json.loads(line.strip())
        source = x[lang]
        target = x['trg']

        if (source is not None) and (target is not None):
            out = '{}\t{}'.format(source, target)
            print(out)


def main():
    args = parse_args()

    try:
        run_main(args.lang)
    except KeyboardInterrupt:
        pass
    except BrokenPipeError:
        pass

