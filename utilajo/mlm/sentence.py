class Sentence:
    def __init__(self, source, index):
        self.source = source
        self.index = index
        self.predictions = {}

    def add_target(self, target):
        self.predictions[target] = None

