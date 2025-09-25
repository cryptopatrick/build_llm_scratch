import re
import urllib.request

################################################################################
# Toknizer
class SimpleTokenizerV1:
    def __init__(self, vocab):
        # We store the vocabulary as a class attribute, for easy access during
        # encode and decode processing.
        self.str_to_int = vocab
        # Inverse vocabulary, where token ids are mapped to text tokens.
        self.int_to_str = {i:s for s, i in vocab.items()}

    def encode(self, text):
        preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
        preprocessed = [item.strip() for item in preprocessed if item.strip()]
        # We replace unknown words with the <|unk|> token.
        preprocessed = [item if item in self.str_to_int
            else "<|unk|>" for item in preprocessed]
        ids = [self.str_to_int[s] for s in preprocessed]
        return ids

    def decode(self, ids):
        text = " ".join([self.int_to_str[i] for i in ids])
        # Remove spaces before these punctuations.
        text = re.sub(r'\s+([,.:;?!"()\'])', r'\1', text)
        return text

################################################################################
# Get file from location.
url = "https://raw.githubusercontent.com/cryptopatrick/build_llm_scratch/refs/heads/master/ch02/code01/the-verdict.txt"
file_path = "the-verdict.txt"
urllib.request.urlretrieve(url, file_path)

# Read file and tokenize it.
with open ("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
all_words = sorted(set(preprocessed))
all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

# TODO: Explain this code. List 50 words in the vocabulary.
vocab = {token:integer for integer, token in enumerate(all_tokens)}
print(len(vocab))

# If we print the last five words, we'll see these tokens.
for i, item in enumerate(list(vocab.items())[-5:]):
  print(item)


tokenizer = SimpleTokenizerV1(vocab)
text = """It's the last he painted, you know, Mrs. Gisburn said with pardonable pride."""
token_ids = tokenizer.encode(text)
print(token_ids)

text_tokens = tokenizer.decode(token_ids)
print(text_tokens)

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
testtext = " <|endoftext|> ".join((text1, text2))
print(testtext)
print(tokenizer.decode(tokenizer.encode(testtext)))