import torch

class Batch:
    pad_id = None

    def __init__(self, sent_list):
        self.sent_list = sent_list

    def make_tensor(self):
        max_len = len(self.sent_list[0])
        lst = [list(sent) + [self.pad_id] * (max_len - len(sent))
                for sent in self.sent_list]
        ten = torch.tensor(lst)

        if torch.cuda.is_available():
            ten = ten.cuda()

        msk = (ten != self.pad_id)

        return ten, msk

