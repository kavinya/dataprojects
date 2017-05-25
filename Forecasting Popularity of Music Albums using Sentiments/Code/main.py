import os
import glob
import sys
from operator import itemgetter # for sort
import cPickle

import plsa

STOP_WORDS_SET = set()

def print_topic_word_distribution(corpus, number_of_topics, topk, filepath):
    """
    Print topic-word distribution to file and list @topk most probable words for each topic
    """
    print ("Writing topic-word distribution to file: " + filepath)
    V = len(corpus.vocabulary) # size of vocabulary
    assert(topk < V)
    f = open(filepath, "w")
    for k in range(number_of_topics):
        word_prob = corpus.topic_word_prob[k, :]
        word_index_prob = []
        for i in range(V):
            word_index_prob.append([i, word_prob[i]])
        word_index_prob = sorted(word_index_prob, key=itemgetter(1), reverse=True) # sort by word count
        f.write("Topic #" + str(k) + ":\n")
        for i in range(topk):
            index = word_index_prob[i][0]
            f.write(corpus.vocabulary[index] + " " + str(word_index_prob[i][1]) + "; ")
        f.write("\n")
        
    f.close()
    
def print_document_topic_distribution(corpus, number_of_topics, topk, filepath):
    """
    Print document-topic distribution to file and list @topk most probable topics for each document
    """
    print ("Writing document-topic distribution to file: " + filepath)
    assert(topk <= number_of_topics)
    f = open(filepath, "w")
    D = len(corpus.documents) # number of documents
    for d in range(D):
        topic_prob = corpus.document_topic_prob[d, :]
        topic_index_prob = []
        for i in range(number_of_topics):
            topic_index_prob.append([i, topic_prob[i]])
        topic_index_prob = sorted(topic_index_prob, key=itemgetter(1), reverse=True)
        f.write("Document #" + str(d) + ":\n")
        for i in range(topk):
            index = topic_index_prob[i][0]
            f.write("topic" + str(index) + " " + str(topic_index_prob[i][1]) + "; ")
        f.write("\n")
        
    f.close()
        
def main(argv):
    print ("Usage: python ./main.py <number_of_topics> <maxiteration>")
    # load stop words list from file
    stopwordsfile = open("stopwords.txt", "r")
    for word in stopwordsfile: # a stop word in each line
        word = word.replace("\n", '')
        word = word.replace("\r\n", '')
        STOP_WORDS_SET.add(word)
    
    corpus = plsa.Corpus() # instantiate corpus
    # iterate over the files in the directory.
    document_paths = ['./texts/grimm_fairy_tales', './texts/tech_blog_posts', './texts/nyt']
    #document_paths = ['./test/']
    for document_path in document_paths:
        for document_file in glob.glob(os.path.join(document_path, '*.txt')):
            document = plsa.Document(document_file) # instantiate document
            document.split(STOP_WORDS_SET) # tokenize
            corpus.add_document(document) # push onto corpus documents list

    corpus.build_vocabulary()
    print ("Vocabulary size:" + str(len(corpus.vocabulary)))
    print ("Number of documents:" + str(len(corpus.documents)))
    
    number_of_topics = int(argv[1])
    max_iterations = int(argv[2])
    corpus.plsa(number_of_topics, max_iterations)
    
    """Writing document topic prob to a file"""
    document_topic_prob = open('document_topic_prob.txt', 'w')
    document_topic_prob.truncate()
    for doc in corpus.document_topic_prob:
        for value in doc:
            document_topic_prob.write(str(value)+" ")
    document_topic_prob.close()
    
    """Writing topic word prob to a file"""
    topic_word_prob = open('topic_word_prob.txt', 'w')
    topic_word_prob.truncate()
    for topic in corpus.topic_word_prob:
        for word in topic:
            topic_word_prob.write(str(word)+" ")
    topic_word_prob.close()
    
    """Writing topic word prob to a file"""
    
    topic_prob = open('topic_prob.txt', 'w')
    topic_prob.truncate()
    for topic in corpus.topic_prob:
        topic_prob.write(str(topic)+" ")
    topic_prob.close()
    #print corpus.document_topic_prob
    #print corpus.topic_word_prob
    #cPickle.dump(corpus, open('./models/corpus.pickle', 'w'))
    
    print_topic_word_distribution(corpus, number_of_topics, 20, "./topic-word.txt")
    print_document_topic_distribution(corpus, number_of_topics, 10, "./document-topic.txt")
    
if __name__ == "__main__":
    main(sys.argv)
