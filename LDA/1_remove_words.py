from usefulFunctions import numberOfWords
from usefulFunctions import getDictionary
from usefulFunctions import writeData
from usefulFunctions import getData

def getUserInput(message):
    n = ''
    while n.isnumeric() == False:
        n = input(message)
    return int(n)

def removeMoreThan(dictionary):
    n = getUserInput("Enter the % where words must be removed if they occur more than that in the data: ")
    if n >= 100 :
        return dictionary
    t = numberOfWords(dictionary)
    remove_thres = t/100
    new_dic = {}
    for key, value in dictionary.items():
        if value <= remove_thres: 
            new_dic[key]=value
    return new_dic 


#Given the dictionary, remove words from the dataset containing less than n entries. 
def removeWordsLessThan(dictionary): 
    n = getUserInput("Enter the minimum number of times a word must occur for it to be used. It must be a positive number: ")
    if n <= 0 :
        return dictionary
    new_dic = {}
    for key, value in dictionary.items():
        if value >= n: 
            new_dic[key]=value
    return new_dic 

#Finally, remove the words from the data that aren't in the dictionary anymore
def removeWords(dictionary,data):
    new_data = []
    for tweet in data:
        new_tweet = []
        for word in tweet: 
            if (word) and (word in dictionary):
                new_tweet.append(word)
        new_data.append(new_tweet)
    return new_data

data=getData("input.txt")
dictionary = getDictionary(data)
dictionary = removeMoreThan(dictionary)
dictionary = removeWordsLessThan(dictionary)
#print(dictionary)
data = removeWords(dictionary, data)
#print(data)

writeData(data, "1_data.txt")
