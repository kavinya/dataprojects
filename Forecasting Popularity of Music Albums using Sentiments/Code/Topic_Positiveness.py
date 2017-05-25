__author__ = 'VISHAL'
import nltk
from nltk.corpus import sentiwordnet as swn
import re

swn.senti_synset('breakdown.n.03')
f = open("topic-word.txt")
for line in f:
    if re.search("Topic #*", line):
        new_file = open("topic_positivity.txt", 'a')
        new_file.write(line)
        new_file.close()
    else:
        line = line.strip('\n')
        words = line.split("; ")
        print words
        new_file = open("topic_positivity.txt", 'a')
        positive_score = 0
        negative_score = 0
        flag = 0
        for word in words:
            if word=="": break
            word_split=word.split()
            # print word_split[0], word_split[1]
            magnitude = float(word_split[1])
            sentiment = swn.senti_synsets(word_split[0], 'a')
            if not sentiment:
                continue
            sentiment_value = list(sentiment)[0]
            test = sentiment_value.pos_score()
            print sentiment_value.pos_score()
            positive_score += magnitude*sentiment_value.pos_score()
            negative_score += magnitude*sentiment_value.neg_score()
        new_file.write(str(positive_score - negative_score))
        new_file.write("\n")
        new_file.close()
f.close()