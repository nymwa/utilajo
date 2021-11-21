import sys
from utilajo.util.template import make_main


def preproc():
    for x in sys.stdin:
        x = x.rstrip('\n').split('\t')
        x = x[0] + '\t' + x[1]
        print(x)


main = make_main(preproc)

