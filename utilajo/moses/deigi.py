import sys
import re
from utilajo.util.template import make_main

def krampo_deigi():
    p = re.compile(r'(?<=[\[\]])(?=\S)|(?<=\S)(?=[\[\]])') # notice that [ and ] is contained in \S

    for x in sys.stdin:
        x = x.strip()
        x = p.sub(' ', x)
        print(x)


def bastono_deigi():
    p = re.compile(r'(?<=\|)(?=\S)|(?<=\S)(?=\|)') # notice that | is contained in \S

    for x in sys.stdin:
        x = x.strip()
        x = p.sub(' ', x)
        print(x)


krampo_deigi_main = make_main(krampo_deigi)
bastono_deigi_main = make_main(bastono_deigi)

