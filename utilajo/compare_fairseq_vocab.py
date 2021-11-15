from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('spm')
    parser.add_argument('fsq')
    args = parser.parse_args()
    return args


def load_spm_tokens(args):
    with open(args.spm) as f:
        spm_tokens = [line.split('\t')[0]
                for line in f]
    return spm_tokens


def load_fsq_tokens(args):
    with open(args.fsq) as f:
        fsq_tokens = [line.split()[0]
                for line in f]
    return fsq_tokens


def main():
    args = parse_args()
    spm_tokens = load_spm_tokens(args)
    fsq_tokens = load_fsq_tokens(args)

    print(set(spm_tokens) - set(fsq_tokens))
    print(set(fsq_tokens) - set(spm_tokens))

