import re #regular expressions package

from usefulFunctions import stringToList
from usefulFunctions import printDataInNiceWay  
from usefulFunctions import getSeperator

sep = getSeperator()

def getData(): 
    with open("1_rawTweetTextAsList.txt", "r") as tweet_file:
        tweets = tweet_file.readlines()
        listOfTweets = stringToList(str(tweets))
        print(len(listOfTweets))
        return listOfTweets 

#This function removes the urls
def removeURL(data):
    cleaned_list = []
    for tweet in data:
        tweet = re.sub(r'http\S+', '', tweet, flags=re.MULTILINE)
        cleaned_list.append(tweet)
    return cleaned_list


#Remove tags of people since we are not interested in the account names for the purposes of this project
def removeTags(data):
    cleaned_list = []
    for tweet in data: 
        line = ''
        tweet=tweet.split(' ')
        for word in tweet: 
            if len(word)>0:
                if word[0]!='@': 
                    line = line+' '+word
        cleaned_list.append(line)
    return cleaned_list

#This function returns a list of hashtags, and gives you the option to remove them if necessary
def getHashTags(data, remove=True):
    cleaned_list = []
    hashtags = []
    for tweet in data: 
        line = ''
        tweet=tweet.split(' ')
        for word in tweet: 
            if len(word)>0:
                if word[0]!='#': 
                    line = line+' '+word
                else:
                    hashtags.append(word)

        cleaned_list.append(line)
    print("Hashtags found: "+str(hashtags))
    return cleaned_list



    


#Remove special characters using the built in regular expression package. All characters that is not numbers or letters are removed. It keeps the . , and ? for readability
def removeSpecialCharacters(data):
    cleaned_list = []
    for tweet in data:
        tweet = re.sub('[^a-zA-Z0-9 .,?\\\]', '', tweet)
        cleaned_list.append(tweet)
    return cleaned_list

#Remove tweets with duplicate text:
def removeTweetsWithDupText(data):
    return list(dict.fromkeys(data))



#Make all the tweets lower case
def lowerCase(data): 
    cleaned_list = []
    for tweet in data:
        tweet = tweet.lower()
        cleaned_list.append(tweet)
    return cleaned_list

    
data = getData()
data = getHashTags(data)
data = removeTweetsWithDupText(data)
data = removeURL(data)
data = removeTags(data)
data = removeSpecialCharacters(data)
data = lowerCase(data)

f = open("2_PreprocessedData.txt", "w")

f.write(sep.join(data))
f.close()
