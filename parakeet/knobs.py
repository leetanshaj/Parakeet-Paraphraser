from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from Levenshtein import distance as levenshtein_distance


class Adequacy():
    def __init__(self, use_gpu = False):
        if use_gpu:
            device= "cuda:0"
        else:
            device = "cpu"

        self.Adequacy = SentenceTransformer("all-mpnet-base-v2", device = device)
    
    def score(self, input_phrase, output_phrase):
        X = self.Adequacy.encode([input_phrase])
        Y = self.Adequacy.encode([output_phrase])
        C = cosine_similarity(X, Y)[0][0]
        return C

class Diversity():
    def __init__(self) -> None:
        pass
    
    def score(self, input_phrase, output_phrase):
        if isinstance(output_phrase, list):
            scores = []
            for i in output_phrase:
                scores.append(self.levenshteinDistance(input_phrase, i))
            return scores
        k = len(input_phrase)
        l = len(output_phrase)
        score = round(((1 - levenshtein_distance(input_phrase.lower(), output_phrase.lower()) / max(k, l, 1)) * 100), 0)
        return score