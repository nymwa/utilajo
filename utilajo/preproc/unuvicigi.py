import sys
from collections import defaultdict
from utilajo.util.template import make_main

def unuvicigi():
    dct = defaultdict(list)

    for line in sys.stdin:
        line = line.rstrip('\n')
        dct[len(line)].append(line)

    indices = list(dct.keys())
    indices.sort()
    for index in indices:
        dct[index].sort()
        for line in dct[index]:
            print(line)


main = make_main(unuvicigi)

