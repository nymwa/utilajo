import sys
from tqdm import tqdm
from argparse import ArgumentParser
import torch
from .util import read_yaml, print_yaml
from .data import Data
from .model import Model

def make_sentence_list(yml):
    return [hypo['text']
            for hypos_dict in yml
            for hypo in hypos_dict['hypos']]


def update_yaml(yml, data):
    for hypos_dict in yml:
        for hypo in hypos_dict['hypos']:
            hypo['mlm_score'] = data.score_dict[hypo['text']]


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--lang', default = 'en')
    parser.add_argument('--arch', default = 'distilroberta-base')
    parser.add_argument('--detokenize', action = 'store_true')
    parser.add_argument('--max-tokens', type = int, default = 10000)
    return parser.parse_args()


def main():
    args = parse_args()
    yml = read_yaml()
    sent_list = make_sentence_list(yml)
    data = Data(args.lang, args.arch, args.detokenize, sent_list)
    loader = data.make_loader(args.max_tokens)
    model = Model(args.arch)

    # calculate score for masked token
    for batch in tqdm(loader, bar_format = '{l_bar}{r_bar}'):
        pred = model.predict(batch)
        data.update_probs(pred, batch)

    # calculate score for sentence
    data.make_score_dict()

    # make output yaml
    update_yaml(yml, data)
    print_yaml(yml)

