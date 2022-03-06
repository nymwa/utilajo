import sys
import re
from utilajo.util.template import make_main

def deigi():
    p = re.compile(r'(?<=[\[\]])(?=\S)|(?<=\S)(?=[\[\]])')

    for x in sys.stdin:
        x = x.strip()
        x = p.sub(' ', x)
        print(x)


deigi_main = make_main(deigi)

