import sys

def main():
    for line in sys.stdin:
        x = line.strip().split()[::-1]
        x = ' '.join(x)
        print(x)

