import sys
from utilajo.util.template import make_main

def run(trans):
    for x in sys.stdin:
        x = x.strip()
        x = x.translate(trans)
        print(x)


def grandigi():
    trans = str.maketrans({
        '[': '［',
        ']': '］'})
    run(trans)


def malgrandigi():
    trans = str.maketrans({
        '［': '[',
        '］': ']'})
    run(trans)


grandigi_main = make_main(grandigi)
malgrandigi_main = make_main(malgrandigi)

