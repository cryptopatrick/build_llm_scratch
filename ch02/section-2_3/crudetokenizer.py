import re
import urllib.request

# Get file from location.
url = "https://raw.githubusercontent.com/cryptopatrick/build_llm_scratch/refs/heads/master/ch02/code01/the-verdict.txt"
file_path = "the-verdict.txt"
urllib.request.urlretrieve(url, file_path)

# Read file and tokenize it.
with open ("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))
# Print the first 30 words.
print(preprocessed[:30])

# Remove duplicate tokens and sort them alphabetically.
all_words = sorted(set(preprocessed))
vocab_size = len(all_words)
print(vocab_size)

# TODO: Explain this code.
vocab = {token:integer for integer, token in enumerate(all_words)}
for i, item in enumerate(vocab.items()):
    print(item)
    if i >= 50:
        break
