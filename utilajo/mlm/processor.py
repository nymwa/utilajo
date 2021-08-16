from .mlm_detokenizer import MLMDetokenizer
from .mlm_tokenizer import MLMTokenizer

class Processor:
    def __init__(self, lang, detokenize, arch):
        self.detokenizer = MLMDetokenizer(lang, detokenize)
        self.tokenizer = MLMTokenizer(arch)

    def make_sentence(self, text):
        raw = self.detokenizer(text)
        encoded = self.tokenizer(raw)
        return encoded

    def make_pair(self, sent, index):
        target = sent[index]
        source = [n for n in sent]
        source[index] = self.tokenizer.mask_id
        return tuple(source), target
