import sys
from collections import defaultdict

def main():
    char_dict = defaultdict(int)
    for line in sys.stdin:
        word_list = line.strip().split()
        for word in word_list:
            for char in word:
                char_dict[char] += 1

    char_list = [char for char in char_dict]
    char_list.sort()
    for char in char_list:
        freq = char_dict[char]
        point = ord(char)
        print('{}\t{}\t{}'.format(char, hex(point), freq))

