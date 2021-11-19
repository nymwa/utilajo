import sys
from utilajo.util.template import make_main

def normalize():
    for line in sys.stdin:
        print(''.join(line.split()))


main = make_main(normalize)

