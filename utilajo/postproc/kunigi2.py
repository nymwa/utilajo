import json
from contextlib import ExitStack
from argparse import ArgumentParser

def parse_args():
    parser = ArgumentParser()
    parser.add_argument('langs')
    parser.add_argument('indices')
    parser.add_argument('sources')
    parser.add_argument('orig')
    return parser.parse_args()


class Corpus:

    def __init__(self, lang, index_path, source_path):
        self.lang = lang
        self.index_path = index_path
        self.source_path = source_path

    def __iter__(self):
        with open(self.index_path) as index_file, open(self.source_path) as source_file:
            for index_line in index_file:
                okay = (index_line.strip() == 'o')
                if okay:
                    source = source_file.readline().strip()
                else:
                    source = None
                yield (self.lang, source)


class Corpora:

    def __init__(self, lang_list, index_list, source_list):
        self.corpora = [
                Corpus(lang, index, source)
                for lang, index, source
                in zip(lang_list, index_list, source_list)]

    def __iter__(self):
        for tup in zip(*self.corpora):
            dct = {}
            for lang, source in tup:
                dct[lang] = source
            yield dct


class Kunigilo:

    def __init__(self, lang_list, index_list, source_list, orig_path):
        self.corpora = Corpora(lang_list, index_list, source_list)
        self.orig_path = orig_path

    def __iter__(self):
        with open(self.orig_path) as orig_file:
            for orig, dct in zip(orig_file, self.corpora):
                dct['trg'] = orig.strip()
                yield json.dumps(dct, ensure_ascii = False)


def main():
    args = parse_args()

    lang_list = args.langs.split(':')
    index_list = args.indices.split(':')
    source_list = args.sources.split(':')
    assert len(lang_list) == len(index_list) == len(source_list)

    ilo = Kunigilo(lang_list, index_list, source_list, args.orig)
    for dct in ilo:
        print(dct)

