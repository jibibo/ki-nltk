import os 
import nltk, re, pprint 
from nltk import word_tokenize
from nltk.probability import FreqDist

# open and read plain text file
path = nltk.data.find('C:/Users/phili/Desktop/TTTV/PAV/tekst/plainCG.txt')
raw = open(path, 'rU').read()
lines = []
for line in raw.split('\n'):
    # !, ? vervangen door .
    replace_excl = line.replace("!", ".")
    replace_quest_mark = replace_excl.replace("?", ".")

    # 't vervangen door not: does't = does not
    pre_processed = replace_quest_mark.replace("n't", " not")

    # analysis corpus: how long are the sentences?
    # append en lowercase maken
    lines.append(pre_processed.lower())
    

# tokenize corpus for analysis
text = ' '.join([str(line) for line in lines])
tokenized_text = nltk.tokenize.word_tokenize(text)
fdist = FreqDist(tokenized_text)
print(lines)


# Analysis corpus
# Main question: How long is your text?

# How many sentences are there?
print(f'The text contains: {len(lines)} sentences')

# How many hapaxes does your corpus have? -> unique words
hapaxes = fdist.hapaxes()
print(f'Amount of hapaxes in text: {len(hapaxes)}')
print(hapaxes)

# How large is the vocabulary?
length = 0
for line in lines:
    for word in line.split(" "):
        length = length + 1
        
print(f'The vocabulary contains: {length} words')

# How long are the sentences?
sentence_length = length / len(lines)
print(f'Average sentence length is: {round(sentence_length)}')

# What are the most frequent words?
print(f'The 30 most frequent words are: {print(fdist.most_common(30))}')
