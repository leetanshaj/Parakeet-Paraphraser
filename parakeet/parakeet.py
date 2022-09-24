from simpletransformers.seq2seq import Seq2SeqModel
from parakeet.knobs import Adequacy, Diversity

class Parakeet():
    def __init__(self, model_tag = "anshaj/Parakeet", use_gpu = False):
        if use_gpu:
            device= "cuda:0"
        else:
            device = "cpu"

        self.Rephraser = Seq2SeqModel(encoder_decoder_type="bart", encoder_decoder_name=model_tag, use_cuda=True)
        self.Adequacy = Adequacy(use_gpu = use_gpu)
        self.Diversity = Diversity()

    def rephrase(self,input_sentence, max_return_sequences = 3, max_length = 128, top_k = 100, top_p = 0.95, return_diversity_score = True, return_similarity_score = True):
        if len(input_sentence)>max_length:
            max_length+=16 
        if max_length>=1024:
            raise Exception(f"Length {len(input_sentence)} more than maximum limit (1024)")
        self.Rephraser.args.num_beams = max_return_sequences
        self.Rephraser.args.num_return_sequences = max_return_sequences
        self.Rephraser.args.max_seq_length = max_length
        self.Rephraser.args.max_length = max_length
        self.Rephraser.args.top_k = top_k
        self.Rephraser.args.top_p = top_p
        predicted = self.Rephraser.predict([input_sentence])
        results = {}
        for i in predicted[0]:
            results[i] = {}
            if return_diversity_score:
                results[i]["diversity"] = self.Diversity.score(input_sentence, i)
            if return_similarity_score:
                results[i]["adequacy"] = self.Adequacy.score(input_sentence, i)
        return results

       
            

        

    