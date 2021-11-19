import sys
from utilajo.util.template import make_main

class Line:

    def __init__(self, sent_list):
        self.sent_list = sent_list
        self.lens = [len(sent) for sent in sent_list]

    def __len__(self):
        return len(self.sent_list)

    def __lt__(self, other):
        assert len(self) == len(other)
        for i in range(len(self)):
            if self.lens[i] < other.lens[i]:
                return True
            elif self.lens[i] > other.lens[i]:
                return False
            elif self.sent_list[i] < other.sent_list[i]:
                return True
            elif self.sent_list[i] > other.sent_list[i]:
                return False
        return True

    def __str__(self):
        return '\t'.join(self.sent_list)


def vicigi():
    xs = [line.rstrip('\n').split('\t')
            for line in sys.stdin]
    xs = [Line(x) for x in xs]
    xs.sort()
    for x in xs:
        print(str(x))


main = make_main(vicigi)

