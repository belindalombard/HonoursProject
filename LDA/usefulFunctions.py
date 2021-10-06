import sys
import numpy as np
from ast import literal_eval 
from munkres import Munkres, print_matrix, make_cost_matrix

#Returns dictionary with the number of times each word occurs 
def getDictionary(data):
    d = {}
    for tweet in data: 
        for word in tweet: 
            if word in d: 
                d[word] = d[word]+1
            else:
                d[word] = 1
    return d 



def numberOfWords(dictionary):
    total = 0
    for key,value in dictionary.items():
        total += value

    return total

def writeData(tweets, filename):
    f = open(filename, "w")
    add = []
    for t in tweets: 
        add.append("|".join(t))
    f.write("#####".join(add))
    f.close()

def getData(filename):
    with open(filename, 'r') as f:
       s = f.readlines() 
       tweets = str(s).split("#####")
       data = []
       for tweet in tweets: 
            data.append(tweet.split("|"))
       return data

def getTopWords(numbers, n): #Returns a list of size n containing the top 5 indexes of a given array
    top_n_array = []
    for i in range(len(numbers)):
        p = numbers[i]
        if p not in top_n_array: 
            if len(top_n_array)<n:
                top_n_array.append(p)
            else:
                minimum = min(top_n_array)
                if p>minimum: 
                    top_n_array[top_n_array.index(minimum)] = p
    return top_n_array

def countScore(result, T): 
    compare_to = result[0]
    scores = []
    for t in range(T): 
        score = 0
        out_of= 0
        for i in range(1, len(result)): 
            for word in result[i][t]: 
                out_of +=1
                if word in compare_to[t]:
                    score +=1
        scores.append(score)
        #print("Topic " + str(t) + ", Score: " + str(score) + ", Out Of " + str(out_of))
    return scores, out_of

def matchTopics(run_zero, compare,  T):
    #Iterate through topics of result   
    res = np.zeros((T, T)) 

    for a in range(T):
        for b in range(T): 
            #count number of matches
            matches = len([w for w in compare[b] if w in run_zero[a]])
            res[a][b] = matches 
    return res

def getTopics(matrix, result):
    m = Munkres()
    cost_mat = make_cost_matrix(matrix, lambda cost: sys.maxsize - cost)
    indexes = m.compute(cost_mat)
    #print(indexes)
    new_topics = []
    for topic in indexes: 
        new = topic[1]
        #print(new)
        new_topics.append(result[new])
    return new_topics

def write_to_file(scores,new_result, T, P, max_score):
    f = open('results_consistency.txt', 'a')
    f2 = open('results_metadata.txt', 'a')
    f.write('\n ------------------------------------------------ \n')
    f2.write('\n ------------------------------------------------ \n')
    f.write("RESULTS FOR " + str(T) + " TOPICS AND " + str(P) + " WORDS\n") 
    f2.write("RESULTS FOR " + str(T) + " TOPICS AND " + str(P) + " WORDS\n") 
    for t in range(T): 
        f.write("TOPIC " + str(t) + ": " )
        f.write("Score: " + str(scores[t]) + '\n')
        f2.write("TOPIC " + str(t) + ": " )
        for res in new_result: 
            f2.write(str(res[t])+'\n') 
    f.write("TOTAL SCORE: " + str(sum(scores)) + " OUT OF " + str(max_score*T)+'\n')
            

def countConsistencyScore(result, P):
    global max_sum
    #print("COUNTING CONSISTENCY SCORE")
    new_result = [] 
    new_result.append(result[0])
    T = len(result[0])
    print(result[0])
    for run in range(1, len(result)):
        matched_topics = matchTopics(result[0], result[run], T)
        check = [0]*T
        max_sum = 0
        new_topics = getTopics(matched_topics, result[run])
        new_result.append(new_topics)
    scores, out_of = countScore(new_result, T)
    write_to_file(scores, new_result, T, P, out_of) 





