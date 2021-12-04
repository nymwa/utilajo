import sys
from argparse import ArgumentParser
from fasttext import load_model

def make_printer(target_label, k, p, rev):

    def k_output(x, lang_labels, probs):
        if (target_label in lang_labels) ^ rev:
            print(x)

    def p_output(x, lang_labels, probs):
        if ((target_label == lang_labels[0]) and (probs[0] >= p)) ^ rev:
            print(x)

    assert (k == 1) or (p is None)
    if (k == 1) and (p is not None):
        f = p_output
    else:
        f = k_output
    return f


def detect(model_path, k=1, p=None, lang='en', rev=False):
    target_label = '__label__{}'.format(lang)
    model = load_model(model_path)
    printer = make_printer(target_label, k, p, rev)

    for line in sys.stdin:
        line = line.strip()
        lang_labels, probs = model.predict(line, k=k)
        printer(x, lang_labels, probs)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('model')
    parser.add_argument('-k', type = int, default = 1)
    parser.add_argument('-p', type = float, default = None)
    parser.add_argument('-l', '--lang', default = 'en')
    parser.add_argument('-r', '--reverse', dest = 'rev', action = 'store_true')
    return parser.parse_args()


def main():
    args = parse_args()
    detect(args.model, args.k, args.p, args.lang, args.rev)

