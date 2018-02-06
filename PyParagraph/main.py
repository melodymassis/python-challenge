#PyParagraph

#import re

filename = "words.txt"
#num_words = 0
#num_sent = 0
#num_let = 0

file = open(filename, 'r')
sourcewords = file.read()
words = sourcewords.split()

num_words = len(words)
print("\n")
print("Paragraph Analysis", "\n")
print("-------------------","\n")
print("Approximate word count: ",num_words)

sentences = sourcewords.split('.')
num_sent = len(sentences)
print("Approximate sentence count: ",num_sent)


num_let = len(sourcewords)
print("Approximate letter count: ",num_let)

avg_let = num_let/num_words
print("Average letter count: ",avg_let)

avg_sen = num_words/num_sent
print("Average Sentence Lenght: ",avg_sen,"\n")
