__author__ = 'VISHAL'
import nltk
from nltk.corpus import sentiwordnet as swn
import re
import numpy

number_topics = 10
ft = open("topic_positivity.txt")
topic_positivity = numpy.zeros(number_topics)
i = 0
for line in ft:
    if re.search("Topic #*", line):
        continue
    else:
        topic_positivity[i] = float(line)
        i += 1
print "hello"
f = open("document-topic.txt")
new_file = open("document_positivity.txt", 'a')
for line in f:
    if re.search("Document #*", line):
        new_file.write(line)
    else:
        line = line.strip('\n')
        words = line.split("; ")
        print words
        document_positivity = open("document_positivity.txt", 'a')
        cumulative_score = 0
        for word in words:
            if word=="": break
            word_split=word.split()
            print word_split[0], word_split[1]
            magnitude = float(word_split[1])
            cumulative_score += magnitude*topic_positivity[int(word[-1:])]
        new_file.write(str(cumulative_score))
        new_file.write("\n")

new_file.close()
f.close()