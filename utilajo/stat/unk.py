import sys
import numpy as np
from collections import defaultdict

class UnkStat:

    def __init__(self):
        self.unk = 0
        self.word = 0
        self.sent = 0

    def add_sent(self, sent):
        for word in sent.strip().split():
            if word == '<unk>':
                self.unk += 1
            self.word += 1
        self.sent += 1


def main():
    stat = UnkStat()
    for x in sys.stdin:
        stat.add_sent(x)

    print('<unk>: {}'.format(stat.unk))
    print('unk / word: {:.2f}%'.format(stat.unk / stat.word * 100))
    print('unk / sent: {:.2f}%'.format(stat.unk / stat.sent * 100))

