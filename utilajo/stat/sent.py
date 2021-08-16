import sys
import numpy as np
from collections import defaultdict

def main():
    len_list = []
    for line in sys.stdin:
        length = len(line.strip().split())
        len_list.append(length)
    len_array = np.array(len_list)

    maximum = len_array.max()
    minimum = len_array.min()
    print('max: {}'.format(maximum))
    print('min: {}'.format(minimum))

    var = len_array.var()
    std = len_array.std()
    print('var: {}'.format(var))
    print('std: {}'.format(std))

    avg = np.mean(len_array)
    print('avg: {}'.format(avg))

    width = 10
    q_index = list(range(width, 100, width))
    q_list = np.percentile(len_array, q_index)
    for index, q in zip(q_index, q_list):
        print('q{}: {}'.format(index, q))

