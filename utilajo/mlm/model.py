import torch
from transformers import AutoModelForMaskedLM

class Model:
    def __init__(self, arch):
        self.model = AutoModelForMaskedLM.from_pretrained(arch)
        self.model.eval()
        if torch.cuda.is_available():
            self.model.cuda()

    def predict(self, batch):
        ten, msk = batch.make_tensor()
        with torch.no_grad():
            pred = self.model(ten, attention_mask = msk)[0]
        return pred

