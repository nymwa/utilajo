import torch
from .batch import Batch

class BatchLoader(list):

    def __init__(self, sent_list, pad_id, max_tokens):
        Batch.pad_id = pad_id
        self.sent_list = sent_list
        self.max_tokens = max_tokens
        self.batches = self.make_batches()
        super().__init__(self.batches)

    def make_batches(self):
        batches = []
        batch = []
        acc = 0
        max_len = len(self.sent_list[0])
        for sent in self.sent_list:
            acc += 1
            if acc * max_len > self.max_tokens:
                batches.append(Batch(batch))
                batch = [sent]
                acc = 1
                max_len = len(sent)
            else:
                batch.append(sent)
        if batch:
            batches.append(Batch(batch))
        return batches

