with open("corpus.txt", "r") as f:
    corpus = f.readline()  # file is 1 line

no_quotes = corpus.replace("\"", "").lower()


no_punctuation = no_quotes.replace(
    "!", "\n").replace("?", "\n").replace(".", "\n")

sentences = no_punctuation.split("\n")

print("\n".join(sentences))
