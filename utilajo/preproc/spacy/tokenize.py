import sys
import spacy

def space_normalization(x):
    return ' '.join(x.split())

class SpacyWrapper:
    def __init__(self, lang):
        self.nlp = spacy.load(lang)

    def line_to_doc(self, line):
        line = line.strip()
        line = space_normalization(line)
        doc = self.nlp.make_doc(line)
        return doc

def tokenize(lang):
    nlp = SpacyWrapper(lang)
    for x in sys.stdin:
        doc = nlp.line_to_doc(x)
        print(' '.join([x.text for x in doc]))

def en():
    tokenize('en_core_web_sm')

def de():
    tokenize('de_core_news_sm')

