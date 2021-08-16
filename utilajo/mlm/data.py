import torch
from .processor import Processor
from .sentence import Sentence
from .loader import BatchLoader
from .scorer import Scorer

class Data:
    def __init__(self, lang, arch, detokenize, text_list):
        self.processor = Processor(lang, detokenize, arch)
        self.text_list = text_list
        self.sent_dict = {sent: self.processor.make_sentence(sent)
                for sent in text_list}
        self.source_dict = {}
        self.make_source_dict()
        self.scorer = Scorer(self)

    def make_source_dict(self):
        for sent in self.sent_dict.values():
            for index in range(1, len(sent) - 1):
                source, target = self.processor.make_pair(sent, index)
                if source not in self.source_dict:
                    self.source_dict[source] = Sentence(source, index)
                self.source_dict[source].add_target(target)

    def make_source_redup_sorted_list(self):
        lst = [x for x in self.source_dict]
        lst = list(set(lst))
        lst.sort(key = lambda x: (-len(x), x))
        return lst

    def make_loader(self, max_tokens):
        sent_list = self.make_source_redup_sorted_list()
        pad_id = self.processor.tokenizer.pad_id
        return BatchLoader(sent_list, pad_id, max_tokens)

    def update_probs(self, pred, batch):
        for logit, source in zip(pred, batch.sent_list):
            sent = self.source_dict[source]
            dist = torch.log_softmax(logit[sent.index], dim = -1)
            for target in sent.predictions:
                log_prob = dist[target].item()
                sent.predictions[target] = log_prob

    def make_score_dict(self):
        self.score_dict = {}
        for text in self.text_list:
            token_list = self.sent_dict[text]
            score = self.scorer.get_score(token_list)
            self.score_dict[text] = score

