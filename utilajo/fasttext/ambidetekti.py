import sys
from argparse import ArgumentParser
from fasttext import load_model

def make_printer(src_label, trg_label, k, p, rev):

    def k_output(src, trg, lang_labels, probs):
        if ((src_label in src_lang) and (trg_label in trg_lang)) ^ rev:
            print('{}\t{}'.format(src, trg))

    def p_output(src, trg, lang_labels, probs):
        if ((((src_label == src_lang[0])
            and (trg_label == trg_lang[0]))
            and (probs[0] >= p))
            ^ rev):
            print('{}\t{}'.format(src, trg))

    assert (k == 1) or (p is None)
    if (k == 1) and (p is not None):
        f = p_output
    else:
        f = k_output
    return f


def detect(model_path, src_lang, trg_lang, k=1, p=None, rev=False):
    src_label = '__label__{}'.format(src_lang)
    trg_label = '__label__{}'.format(trg_lang)
    model = load_model(model_path)
    printer = make_printer(src_label, trg_label, k, p, rev)

    for line in sys.stdin:
        line = line.rstrip('\n')
        src, trg = line.split('\t')
        src_lang = model.predict(src, k=k)[0]
        trg_lang = model.predict(trg, k=k)[0]
        printer(src, trg, lang_labels, probs)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('model')
    parser.add_argument('src_lang')
    parser.add_argument('trg_lang')
    parser.add_argument('-k', type=int, default=1)
    parser.add_argument('-p', type = float, default = None)
    parser.add_argument('-r', '--reverse', dest='rev', action = 'store_true')
    return parser.parse_args()


def main():
    args = parse_args()
    detect(args.model, args.src_lang, args.trg_lang, args.k, args.p, args.rev)

