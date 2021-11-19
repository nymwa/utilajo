import sys
import re
from utilajo.util.template import make_main

p1 = re.compile(r'|'.join(['</?{}[^>]*>'.format(x)
    for x in ['doc', 'speaker', 'reviewer', 'translator', 'url', 'talkid', 'keywords']]))
p2 = re.compile(r'<title>|</title>|<description>|</description>')


def cond(x):
    return not p1.search(x)


def preproc_line(x):
    x = p2.sub('', x)
    return x

def preproc():
    for x in sys.stdin:
        x = x.strip()
        if cond(x):
            x = preproc_line(x)
            x = ' '.join(x.split())
            print(x)


main = make_main(preproc)

