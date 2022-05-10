from dataclasses import replace
import re


with open("corpus.txt", "r") as f:
    corpus = f.readline() 

no_quotes = corpus.replace("\"", "").lower()

no_punctuation = no_quotes.replace("!", "!\n").replace("?", "?\n").replace(".", ".\n").replace("-", " ")

print("\n".join(no_punctuation.split("\n")))

sentences = no_punctuation.split("\n")

print("\n".join(sentences))
