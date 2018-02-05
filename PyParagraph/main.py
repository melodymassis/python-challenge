#PyParagraph


import re

#filename = "words.txt"

words = "the quick brown fox jumps. Over the fence".split()
#print(words)

#idx_to_words = {i:w for i,w in enumerate(words)}
#print(idx_to_words)

num_words = len(words)
print("Approximate word count ")
print(num_words)

sentences = "the quick brown. fox jumps. Over the fence".split('.')
num_sent = len(sentences)
print("Approximate sentence count ")
print(num_sent)
