# Count the 10 most frequent words in a text file
import string
from collections import Counter

# Read and process the file
with open("sample-file.txt", "r") as f:
    text = f.read()

# Split into tokens, clean, and filter
tokens = text.split()
cleaned_tokens = []
for token in tokens:
    token = token.lower().strip(string.punctuation)
    if sum(c.isalpha() for c in token) >= 2:
        cleaned_tokens.append(token)

# Count frequencies
freq = Counter(cleaned_tokens)

# Print 10 most frequent words
for word, count in freq.most_common(10):
    print(f"{word} -> {count}")