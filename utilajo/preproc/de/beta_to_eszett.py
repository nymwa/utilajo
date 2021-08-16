import sys

def main():
    beta = chr(0x3b2)
    eszett = chr(0xdf)

    for line in sys.stdin:
        x = line.strip().replace(beta, eszett)
        print(x)

