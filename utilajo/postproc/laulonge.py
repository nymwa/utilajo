import sys
from utilajo.util.template import make_main

def laulonge():
    for x in sys.stdin:
        x = x.strip()
        x = x.split('\t')
        print('-----')
        for line in x:
            print(line)


main = make_main(laulonge)

