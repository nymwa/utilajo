import sys
import yaml
from argparse import ArgumentParser
from reguligilo.decoder import Decoder

space = chr(0x2581)
decoder = Decoder()


def replace_unk(token, unk_token, unk_char):
    if token == unk_token:
        x = unk_char
    else:
        x = token
    return x


def sort_by_score(args, lst):
    if args.r2l and args.mlm:
        key = lambda x : (x['score'] + x['r2l_score']) / 2 + args.l * x['mlm_score']
    elif args.mlm:
        key = lambda x : x['score'] + args.l * x['mlm_score']
    elif args.r2l:
        key = lambda x : (x['score'] + x['r2l_score']) / 2
    else:
        key = lambda x : x['score']

    lst.sort(key = key)


def print_best(args, lst):
    x = lst[-1]['text']
    x = x.strip()
    x = x.split()

    if args.reverse:
        x = x[::-1]

    if not args.retain_unk:
        x = [replace_unk(token, args.unk_token, args.unk_char) for token in x]

    x = ''.join(x)
    if not args.retain_whitespace:
        x = x.replace(space, ' ')
        x = x.strip()

    if not args.retain_normalized:
        x = decoder(x)

    if args.show_score:
        score = lst[-1]['score']
        x = '{}\t{}'.format(score, x)

    print(x)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-s', '--show-score', action = 'store_true')
    parser.add_argument('-r', '--reverse', action = 'store_true')
    parser.add_argument('-l', type = float, default = None)
    parser.add_argument('--r2l', action = 'store_true')
    parser.add_argument('--mlm', action = 'store_true')
    parser.add_argument('-u', '--unk-char', default = '⁇')
    parser.add_argument('--unk-token', default = '<unk>')
    parser.add_argument('--retain-unk', action = 'store_true')
    parser.add_argument('--retain-whitespace', action = 'store_true')
    parser.add_argument('--retain-normalized', action = 'store_true')
    return parser.parse_args()


def main():
    args = parse_args()

    yml = yaml.safe_load(sys.stdin)

    for hypos_dict in yml:
        hypos = hypos_dict['hypos']
        sort_by_score(args, hypos)
        print_best(args, hypos)

