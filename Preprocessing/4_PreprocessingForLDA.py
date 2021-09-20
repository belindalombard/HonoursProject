
import re
from usefulFunctions import stringToList
from usefulFunctions import printDataInNiceWay  
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def getData(): 
    with open("3_Tweets.txt","r") as tweet_file:
        tweets = tweet_file.readlines()
        listOfTweets = stringToList(str(tweets))
        print(len(listOfTweets))
        return listOfTweets 

#Function to tokenize Tweets
def tokenization(tweets):
    tokenized_set = []
    for t in tweets: 
        tokenized_set.append(t.split())
    return tokenized_set


#Remove all punctution
def removePunc(tweets): 
    out=[]
    for t in tweets: 
        row=[]
        for w in t:
            word = w.replace("\\n", "").replace("\\", "").replace(".","").replace("?","").replace(",","")
            row.append(word)
        out.append(row)
    return out



#Remove short words
def removeShortWords(tweets):
    out=[]
    for t in tweets: 
        row=[]
        for w in t:
            if len(w)>=5:
                row.append(w)
        out.append(row)
    return out

#Stemming 
def stem(tweets):
    ps = PorterStemmer()
    out=[]
    for t in tweets: 
        row=[]
        for w in t: 
            row.append(ps.stem(w))
        out.append(row)
    return out

#Lemmatizer
def lemmatize(tweets):
    lemmatizer = WordNetLemmatizer()

    out=[]
    for t in tweets: 
        row=[]
        for w in t: 
            row.append(lemmatizer.lemmatize(w))
        out.append(row)
    return out


#Remove Stopwrds
def stopwrds(tweets):
    lemmatizer = WordNetLemmatizer()

    out=[]
    for t in tweets: 
        row=[]
        for w in t: 
            if w not in stopwords.words('english'):
                row.append(w)
        out.append(row)
    return out


    

#Print tweets (this is just for testing purposes)
def printList(tweets):
    for row in tweets:
        print(row)


def writeData(tweets):
    f = open("4_PreprocessedData.txt", "w")
    add = []
    for t in tweets: 
        add.append("|".join(t))
    f.write("#####".join(add))
    f.close()

def removeBlanks(tweets):
    out=[]
    for t in tweets: 
        row=[]
        for w in t: 
            strip = "".join(w.split())
            if strip!='':
                row.append(strip)
        if len(row)>0:
            out.append(row)
    return out



tweets = getData()
tweets = tokenization(tweets)
tweets = removePunc(tweets)
tweets = removeShortWords(tweets)
tweets = lemmatize(tweets)
tweets = stem(tweets)
tweets = stopwrds(tweets)
tweets = removeBlanks(tweets)
writeData(tweets)
#printList(tweets)





