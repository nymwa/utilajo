import sys
from utilajo.util.template import make_main

def preproc():
    for x in sys.stdin:
        x = x.strip()
        x = x.lower()
        print(x)


main = make_main(preproc)

