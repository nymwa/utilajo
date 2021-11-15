import sys
from collections import defaultdict
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-f', '--sort-by-freq', action = 'store_true')
    return parser.parse_args()


def make_char_dict():
    char_dict = defaultdict(int)

    for line in sys.stdin:
        word_list = line.strip().split()
        for word in word_list:
            for char in word:
                char_dict[char] += 1

    return char_dict


def make_char_list(
        char_dict,
        sort_by_freq = False):

    char_list = [(char, char_dict[char]) for char in char_dict]

    if sort_by_freq:
        char_list.sort(key = lambda x: (-x[1], x[0]))
    else:
        char_list.sort(key = lambda x: x[0])

    return char_list


def show(char_list):
    for char, freq in char_list:
        point = ord(char)
        print('{}\t{}\t{}'.format(char, hex(point), freq))


def main():
    args = parse_args()

    char_dict = make_char_dict()
    char_list = make_char_list(
            char_dict,
            sort_by_freq = args.sort_by_freq)
    show(char_list)

