import urllib.request

# Location of text to use for input.
url = "https://raw.githubusercontent.com/cryptopatrick/build_llm_scratch/refs/heads/master/ch02/code01/the-verdict.txt"
file_path = "the-verdict.txt"
urllib.request.urlretrieve(url, file_path)

with open ("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text = f.read()

print("Total number of chars:", len(raw_text))
print("First 100 characters in the file: ")
print(raw_text[:99])

