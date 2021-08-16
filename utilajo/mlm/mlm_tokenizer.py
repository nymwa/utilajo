from transformers import AutoTokenizer

class MLMTokenizer:
    def __init__(self, name):
        self.name = name
        self.tokenizer = AutoTokenizer.from_pretrained(name)
        self.pad_id = self.tokenizer.vocab[self.tokenizer.pad_token]
        self.mask_id = self.tokenizer.vocab[self.tokenizer.mask_token]

    def encode(self, x):
        x = x.strip()
        x = self.tokenizer(x)['input_ids']
        return x

    def __call__(self, x):
        return self.encode(x)

