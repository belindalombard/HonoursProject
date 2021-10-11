import json
import sys 
from usefulFunctions import getSeperator

f = open("1_rawTweetTextAsList.txt", "w") #List seperating tweets with "#####"
f2 = open("1_rawTweetsInReadableFormat.txt", "w") #Open tweets in a more readable format

count=0

#Seperator: 
sep = getSeperator()

#Write tweet text to a raw format
def writeTweets():
    with open("data.json") as dfile: 
        d = json.load(dfile)
        listOfTweets=[]
        
        for tweet in d:
            #Need to see if seperator is in tweet text and remove it if it is
            text=tweet['text']
            check = False
            while check is False: 
                if sep in text:
                    text.remove(sep)
                else: 
                    check=True
            
            global count
            count += 1
            f.write(text+sep)
            f2.write("Tweet " + str(count) + ": [" + text + "]\n")

writeTweets()
f.close()
f2.close()
print(count)


