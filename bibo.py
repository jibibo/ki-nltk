import nltk, re, pprint
from nltk import word_tokenize
from nltk.probability import FreqDist


# open and read
with open("corpus.txt", "r") as f:
    corpus = f.readline()  # file is 1 line


# preprocessing
lower = corpus.lower()
no_abbreviations = lower.replace("n't", " not")
no_quotes = no_abbreviations.replace("\"", "")
no_punctuation = no_quotes.replace(
    "!", "\n").replace("?", "\n").replace(".", "\n")

sentences = no_punctuation.split("\n")


# print text
print("\n".join(sentences))


# frequency distribution
joined_text = ' '.join(sentences)
tokenized_text = nltk.tokenize.word_tokenize(joined_text)
fdist = FreqDist(tokenized_text)


# show corpus stats
print(f"sentences: {len(sentences)}")

hapaxes = len(fdist.hapaxes())