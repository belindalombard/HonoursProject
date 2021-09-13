from usefulFunctions import getData
from random import randrange
import numpy as np
from usefulFunctions import numberOfWords
from usefulFunctions import getDictionary

def assignRandomTopics(data, T):
    topics = []
    #print(data)
    for tweet in data: 
        line = []
        for word in tweet:
            line.append(randrange(0,T))
        topics.append(line) 
    return topics

def createTweetTopicMatrix(T, topic_assignment):
    tweet_topic = np.zeros((T, len(topic_assignment)))
    tweet_number = 0
    for tweet in topic_assignment: 
        for topic_number in tweet: 
            tweet_topic[topic_number, tweet_number] += 1
        tweet_number += 1
    return tweet_topic
            

#STOP HERE - COUNTS ARE NOT WORKING CORRECTLY 
def createTopicWordMatrix(data, T, topic_assignment, N, words): 
    word_topic = np.zeros((T, N))
    tweet_number = 0
    for tweet in data:
        word_number = 0
        for word in tweet:
            topic_number = topic_assignment[tweet_number][word_number] 
            w = words.index(word)
            word_topic[topic_number, w] +=1
            word_number += 1
        tweet_number += 1
    return word_topic


#TEST METHOD: Print the topic word matrix
def printTopicWords(words, topic_word):
    i = 0 
    for word in words: 
        print(word + ":  "  + str(topic_word[ : , i]))
        i += 1


def LDA():
    data = getData("1_data.txt")

    #Get the number of topics
    while True: 
        try: 
            T = int(input("Enter the number of topics: "))
        except ValueError: 
            print("Please enter a valid number")
        else: 
            break

    topic_assignment = assignRandomTopics(data, T)
    #print(topic_assignment)
    tweet_topic = createTweetTopicMatrix(T, topic_assignment) 
    np.set_printoptions(threshold=np.inf)
    #print(tweet_topic)

    #Get number of distinct words and the dictionary
    dictionary = getDictionary(data)
    words = list(dictionary.keys())
    number_of_words = len(words)  
    topic_word = createTopicWordMatrix(data, T, topic_assignment, number_of_words, words) 
    printTopicWords(words, topic_word) 

LDA()
