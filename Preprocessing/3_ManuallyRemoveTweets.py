from usefulFunctions import stringToList 
from usefulFunctions import getSeperator

sep = getSeperator()

def writeToFile(tweets):
    a = open("3_Tweets.txt", "a") 
    a.write(sep.join(tweets)+sep)
    a.close()


def removeTweets(i):
    with open("2_PreprocessedData.txt") as f: 
        data = f.readlines()
        tweets = stringToList(str(data))

        finalTweets = []
        
        for k in range(i, len(tweets)): 
            print("Are you planning on keeping tweet " + str(k) + "?" )
            print(tweets[k]) 
            keep = input("y or n (or s to stop): ")
            
            if (keep.lower() == "y"):
                finalTweets.append(tweets[k])
            
            if (keep.lower() == "s"):
                writeToFile(finalTweets)
                print("Remember that you need to start at tweet " + str(k) + " next time")
                break

i = input("At which tweet do you have to start? ")
removeTweets(int(i))
