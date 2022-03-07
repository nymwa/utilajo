import sys
from utilajo.util.template import make_main

def grandigi():
    for x in sys.stdin:
        x = x.strip()
        x = x.replace('|', '｜')
        print(x)


def malgrandigi():
    for x in sys.stdin:
        x = x.strip()
        x = x.replace('｜', '|')
        print(x)


grandigi_main = make_main(grandigi)
malgrandigi_main = make_main(malgrandigi)

