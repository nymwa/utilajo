import sys
import json
from utilajo.util.template import make_main

def laulonge2():
    for i, line in enumerate(sys.stdin):
        dct = json.loads(line.strip())
        print('{}\t--- --- ---'.format(i))
        for k, v in dct.items():
            print('{}\t{}'.format(k, v))


main = make_main(laulonge2)

