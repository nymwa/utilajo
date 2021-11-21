import re
import sys
from utilajo.util.template import make_main

src_pattern = re.compile(r'^<source[^>]*>(.*)</source>$')
trg_pattern = re.compile(r'^<target[^>]*>(.*)</target>$')

def preproc():
    src = None
    trg = None
    for x in sys.stdin:
        x = x.strip()
        if x.startswith('<segment'):
            src = None
            trg = None
        elif src_pattern.match(x):
            src = src_pattern.findall(x)[0]
        elif trg_pattern.match(x):
            trg = trg_pattern.findall(x)[0]
        elif x.startswith('</segment'):
            if src is None or trg is None:
                assert False
            print('{}\t{}'.format(src, trg))
            src = None
            trg = None


main = make_main(preproc)

