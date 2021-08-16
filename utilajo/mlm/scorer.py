class Scorer:
    def __init__(self, data):
        self.data = data

    def get_score(self, token_list):
        log_prob_list = []
        for index in range(1, len(token_list) - 1):
            source, target = self.data.processor.make_pair(token_list, index)
            log_prob = self.data.source_dict[source].predictions[target]
            log_prob_list.append(log_prob)
        penalty = (5 + len(log_prob_list)) / (5 + 1)
        score = sum(log_prob_list) / penalty
        return score

