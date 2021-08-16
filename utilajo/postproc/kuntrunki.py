import sys
import json
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('lang_list')
    parser.add_argument('-r', '--ratio', type=float, default=2.0)
    parser.add_argument('--remove-target-without-source', action='store_true')
    return parser.parse_args()


def main():
    args = parse_args()

    lang_list = args.lang_list.split(':')
    th = args.ratio

    for x in sys.stdin:
        x = x.strip()
        x = json.loads(x)

        trg_len = len(x['trg'].split())

        if args.remove_target_without_source and all(x[lang] is None for lang in lang_list):
            continue

        for lang in lang_list:
            if x[lang] is not None:
                src_len = len(x[lang].split())
                if not ((src_len <= trg_len * th) and (trg_len <= src_len * th)):
                    x[lang] = None

        x = json.dumps(x, ensure_ascii = False)
        print(x)

