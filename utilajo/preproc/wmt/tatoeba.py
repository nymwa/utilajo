import sys
from utilajo.util.template import make_main


def preproc():
    for x in sys.stdin:
        x = x.rstrip('\n').split('\t')
        x = x[1] + '\t' + x[3]
        print(x)


main = make_main(preproc)

