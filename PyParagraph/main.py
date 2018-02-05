#PyParagraph


import re

#filename = "words.txt"

words = "the quick brown fox jumps. Over the fence".split()
#print(words)

#idx_to_words = {i:w for i,w in enumerate(words)}
#print(idx_to_words)

num_words = len(words)
print("\n")
print("Paragraph Analysis", "\n")
print("-------------------","\n")
print("Approximate word count: ",num_words)

sentences = "the quick brown. fox jumps. Over the fence".split('.')
num_sent = len(sentences)
print("Approximate sentence count: ",num_sent)


num_let = len("the quick brown. fox jumps. Over the fence")
print("Approximate letter count: ",num_let)

avg_let = num_let/num_words
print("Average letter count: ",avg_let)

avg_sen = num_words/num_sent
print("Average Sentence Lenght: ",avg_sen,"\n")
