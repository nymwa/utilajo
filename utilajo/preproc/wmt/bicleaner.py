import re
import sys
import html
from argparse import ArgumentParser
from utilajo.util.template import make_main

src_pattern = re.compile(r'^<source[^>]*>(.*)</source>$')
trg_pattern = re.compile(r'^<target[^>]*>(.*)</target>$')

seg_pattern = re.compile(r'^<seg>(.*)</seg>$')

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('target')
    return parser.parse_args()


def preproc(args):
    src_tuv = '<tuv xml:lang="{}">'.format(args.source)
    trg_tuv = '<tuv xml:lang="{}">'.format(args.target)

    flag = 'none'
    src = None
    trg = None

    for x in sys.stdin:
        x = x.strip()
        if (not x.startswith('<tuv')) and x.startswith('<tu'):
            flag = 'tu'

        elif x == src_tuv:
            flag = 'src'

        elif x == trg_tuv:
            flag = 'trg'

        elif seg_pattern.match(x):
            if flag == 'src':
                src = html.unescape(seg_pattern.findall(x)[0])
            elif flag == 'trg':
                trg = html.unescape(seg_pattern.findall(x)[0])
            else:
                assert False

        elif x.startswith('</tu>'):
            flag = 'none'
            assert (src is not None) and (trg is not None)
            print('{}\t{}'.format(src, trg))
            src = None
            trg = None

main = make_main(preproc, parse_args = parse_args)

