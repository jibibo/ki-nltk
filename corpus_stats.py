# get corpus stats

import nltk
from nltk.probability import FreqDist


with open("corpus.txt", "r") as f:
    lines = f.readlines()

print(f"Sentences: {len(lines)}")

words = set()
word_count = 0
for line in lines:
    for word in line.split():
        word_count += 1
        if word not in words:
            words.add(word)

print(f"Word count: {word_count}, unique: {words} ({len(words)})")

one_liner = ' '.join(lines)
tokenized_text = nltk.tokenize.word_tokenize(one_liner)
fdist = FreqDist(tokenized_text)

hapaxes = fdist.hapaxes()
print(f"Hapaxes: {hapaxes} ({len(hapaxes)})")

average_length = word_count / len(lines)
print(f"Average sentence length: {average_length}")

print(f"Top 10 common words: {fdist.most_common(10)}")

with open("all_words.txt", "w") as f:
    for word in fdist.keys():
        f.write(f" -> {word}\n")
