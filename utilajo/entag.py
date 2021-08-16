import sys

def run(tag):
    for line in sys.stdin:
        x = line.strip()
        x = tag + ' ' + x
        print(x)


def gec():
    run('<gec>')


def de():
    run('<de>')


def en():
    run('<en>')


def d2e():
    run('<d2e>')


def e2d():
    run('<e2d>')

