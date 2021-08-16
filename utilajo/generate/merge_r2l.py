import sys
import yaml
from argparse import ArgumentParser
from collections import defaultdict

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('output')
    return parser.parse_args()


def load_output(output_path):
    with open(output_path) as f:
        yml = yaml.safe_load(f)
    return yml


def read_r2l_dict():
    dct = defaultdict(dict)
    for x in sys.stdin:
        x = x.rstrip('\n').split('\t')
        score = float(x[0])
        source = x[1]
        hypothesis = x[2]
        dct[source][hypothesis] = score
    return dct


def main():
    args = parse_args()
    yml = load_output(args.output)
    r2l_dict = read_r2l_dict()

    for hypos_dict in yml:
        hypos = hypos_dict['hypos']
        source = hypos_dict['source']
        for hypo in hypos:
            score = r2l_dict[source][hypo['text']]
            hypo['r2l_score'] = score

    yml = yaml.safe_dump(yml, allow_unicode = True)
    print(yml)

