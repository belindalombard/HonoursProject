###PARAMETERS
iterations = 20
alpha = 0.01 #Hyperparameter
beta = 0.3 #Hyperparameter
n = 10 #Number of words to get from each topic
nruns = 10 #Number of runs 
#----------------------------------------------


from usefulFunctions import getData
from random import randrange
import numpy as np
from usefulFunctions import numberOfWords
from usefulFunctions import getDictionary
from usefulFunctions import getTopWords
from usefulFunctions import countConsistencyScore
import sys

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


def printTopicWords(words, topic_word):
    i = 0 
    for word in words: 
        print(word + ":  "  + str(topic_word[ : , i]))
        i += 1

def calculate_topic_tweet_prob(tweet_topic, alpha, num_words_tweet, T, topic_number, tweet_number):
    probability_num = tweet_topic[topic_number][tweet_number] + alpha
    probability_den = num_words_tweet - 1 + (T*alpha)
    return probability_num/probability_den

def calculate_word_topic_prob(topic_word, beta, word_number, tweet_number, data, T, dict_index, number_of_words_in_tweet, dict_length):
    probability_num = topic_word[T][dict_index] + beta
    probability_den = number_of_words_in_tweet + dict_length*beta
    return probability_num/probability_den

def reassignWords(topic_word, tweet_topic, data, topic_assignment, T, words, alpha, beta): 
    tweet_number = 0
    dict_length = len(words)
    reassign = 0  # NOT ESSENTIAL, TESTING
    not_reassign = 0  #NOT ESSENTIAL, TESTING 
    for t in data: 
        word_number = 0
        number_of_words_in_tweet = len(t)
        for word in t: 
            probabilities = []
            dict_index = words.index(word)
            for i in range(T): #Iterate through each topic to calculate the probabilities
                p1 = calculate_topic_tweet_prob(tweet_topic, alpha, number_of_words_in_tweet, T, i, tweet_number)
                p2 = calculate_word_topic_prob(topic_word, beta, word_number, tweet_number, data, i, dict_index, number_of_words_in_tweet, dict_length)
                probabilities.append(p1*p2)

            new_topic = probabilities.index(max(probabilities))
            old_topic = topic_assignment[tweet_number][word_number]
            
            if new_topic != old_topic: #Reassign word
                topic_word[old_topic][dict_index] -= 1
                topic_word[new_topic][dict_index] += 1
                tweet_topic[old_topic][tweet_number] -= 1
                tweet_topic[new_topic][tweet_number] += 1

                topic_assignment[tweet_number][word_number] = new_topic
                reassign+=1
                #print("Reassigning " + word + " from topic " + str(old_topic) + " to " + str(new_topic))
            else:
                #print("Not reassigning word " + word)
                not_reassign += 1
            word_number += 1
        tweet_number +=1
    
    prop = float(reassign)/float(not_reassign+reassign)  
    #print("Proportion of words reassigned: " + str(prop))
    return topic_word, tweet_topic, topic_assignment, prop 


#This method prints the topic assignments in a readable format
def outputTopicAssignment(topic_word, words, n): 
    topic_number = 0
    for topic in topic_word:
        top_word_indexes = getTopWords(topic, n) 
        print(top_word_indexes)
        w = [] 
        for index in top_word_indexes: 
           w.append(words[int(index)])
        print(str(topic_number) +": " + str(w))      
        topic_number+=1

#This methods return the top n words for each topic
def getTopicAssignment(topic_word, words, n): 
    all_topics = []
    for topic in topic_word:
        top_word_indexes = getTopWords(topic, n) 
        #print(top_word_indexes)
        w = [] 
        for index in top_word_indexes: 
           w.append(words[int(index)])
        all_topics.append(w)
    return(all_topics) 


def numberOfRunsEst(topic_word, tweet_topic, data, topic_assignment, T, words):
    prop = 1
    runs = 0
    while (prop != 0): 
        topic_word, tweet_topic, topic_assignment, prop = reassignWords(topic_word, tweet_topic, data, topic_assignment, T, words, alpha, beta)
        runs += 1
    print("Number of runs: " + str(runs) + 'for number of topics ' + str(T))


def con(data, T, P, NumRuns = 20):
    res = []
    for i in range(10):
        print(i)
        print("LOOKING AT NUMBER OF RUNS")
        topic_assignment = assignRandomTopics(data, T)
        tweet_topic = createTweetTopicMatrix(T, topic_assignment) 
        np.set_printoptions(threshold=np.inf)

        #Get number of distinct words and the dictionary
        dictionary = getDictionary(data)
        words = list(dictionary.keys())
        number_of_words = len(words)  
        topic_word = createTopicWordMatrix(data, T, topic_assignment, number_of_words, words) 

        for k in range(NumRuns): 
            topic_word, tweet_topic, topic_assignment, prop = reassignWords(topic_word, tweet_topic, data, topic_assignment, T, words, alpha, beta)
        res.append(getTopicAssignment(topic_word, words, P))
    countConsistencyScore(res, P)
          

def LDA():
    data = getData("1_data.txt")

    #Get the number of topics
    if len(sys.argv) > 1: 
        T = int(sys.argv[1])
    else:
        while True: 
            try: 
                T = int(input("Enter the number of topics: "))
            except ValueError: 
                print("Please enter a valid number")
            else: 
                break
    if len(sys.argv) > 2:
        arg = sys.argv[2]
        if int(arg) == 0:  #NUMBER OF REQUIRED ITERATIONS ESTIMATED
            topic_assignment = assignRandomTopics(data, T)
            tweet_topic = createTweetTopicMatrix(T, topic_assignment) 
            np.set_printoptions(threshold=np.inf)

            #Get number of distinct words and the dictionary
            dictionary = getDictionary(data)
            words = list(dictionary.keys())
            number_of_words = len(words)  
            topic_word = createTopicWordMatrix(data, T, topic_assignment, number_of_words, words) 
            numberOfRunsEst(topic_word, tweet_topic, data, topic_assignment, T, words)

        if int(arg) == 1: #CONSISTENCY SCORES CALCULATED
            P = int(sys.argv[3])
            con(data, T, P, 5)
    
    elif len(sys.argv)==1: #RUN NORMAL LDA ONCE 
        topic_assignment = assignRandomTopics(data, T)
        tweet_topic = createTweetTopicMatrix(T, topic_assignment) 
        dictionary = getDictionary(data)
        words = list(dictionary.keys())
        number_of_words = len(words)  
        topic_word = createTopicWordMatrix(data, T, topic_assignment, number_of_words, words) 
        
        for i in range(iterations):
            print("Iteration: " + str(i))
            topic_word, tweet_topic, topic_assignment, prop = reassignWords(topic_word, tweet_topic, data, topic_assignment, T, words, alpha, beta)
        
        print(outputTopicAssignment(topic_word, words, n))

 
LDA()
