import re
text ="If a technological feat is possible, man will do it."

# Split on whitespace.
# This will not separate the punctuation in 'it.', or the comma in 'possible,'.
result = re.split(r'(\s)', text)
print(result)

# Split on whitespace or punctuation or comma.
better_result = re.split(r'([,.]|\s)', text)
print(better_result)

# Remove whitespace.
even_better_result = [item for item in better_result if item.strip()]
print(even_better_result)

# Handle additional special characters.
text = "Hello, world. Is this-- a test?"
final_version = re.split(r'([,.:;?_!"()\']|--|\s)', text)
final_version = [item.strip() for item in final_version if item.strip()]
print(final_version)

# Applying tokenizer to text.
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))