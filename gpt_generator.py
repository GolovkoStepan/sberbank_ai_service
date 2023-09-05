from transformers import GPT2LMHeadModel, GPT2Tokenizer


class GptGenerator:
    MODEL_NAME = "sberbank-ai/rugpt3large_based_on_gpt2"

    def __init__(self):
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.MODEL_NAME)
        self.model = GPT2LMHeadModel.from_pretrained(self.MODEL_NAME).cpu()

    def generate(self, text):
        input_ids = self.tokenizer.encode(text, return_tensors="pt").cpu()
        out = self.model.generate(input_ids.cpu(), max_length=50)

        return list(map(self.tokenizer.decode, out))[0]
