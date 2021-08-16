from sacremoses import MosesDetokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from reguligilo.decoder import Decoder

space = chr(0x2581)
decoder = Decoder()

def remove_bpe(x):
    x = x.strip()
    x = x.split()
    x = ''.join(x)
    x = x.replace(space, ' ')
    x = x.strip()
    return x


class MLMDetokenizer:
    def __init__(self, lang, detokenize):
        self.lang = lang
        self.is_detokenize = detokenize

        if self.is_detokenize:
            self.md = MosesDetokenizer(lang = lang)

    def decode(self, x):
        x = x.strip()
        x = remove_bpe(x)
        x = decoder(x)
        return x

    def detokenize(self, x):
        x = x.strip()
        if self.is_detokenize:
            x = self.md.detokenize(x.split())
            if self.lang == 'en':
                x = TreebankWordDetokenizer().detokenize(x.split())
        return x

    def __call__(self, x):
        x = self.decode(x)
        x = self.detokenize(x)
        return x

