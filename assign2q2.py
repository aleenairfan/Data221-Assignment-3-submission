# Count the 5 most frequent bigrams in a text file

import string
from collections import Counter

with open("sample-file.txt", "r") as f:
    text = f.read()

tokens = text.split()
cleaned_tokens = []
for token in tokens:
    token = token.lower().strip(string.punctuation)
    if sum(c.isalpha() for c in token) >= 2:
        cleaned_tokens.append(token)

# Construct bigrams
bigrams = [(cleaned_tokens[i], cleaned_tokens[i+1]) for i in range(len(cleaned_tokens)-1)]
bigram_freq = Counter(bigrams)

# Print 5 most frequent bigrams
for (w1, w2), count in bigram_freq.most_common(5):
    print(f"{w1} {w2} -> {count}")