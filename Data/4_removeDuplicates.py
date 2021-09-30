totalTweets = 0
totalLocation = 0

tweet_ids = [] 

import json

def removeDuplicates(filename):
    with open(filename) as data_file:  
        global tweet_ids
        d = json.load(data_file)
        f_write = open("dup_" + filename, 'w')
        data = []
        for tweet in d['data']:
            tweet_id = tweet['tweet_id']
            if tweet_id not in tweet_ids:
                data.append(tweet)
                tweet_ids.append(tweet_id)
        json.dump(data, f_write)

        #This removes the trailing , and replace it with closing brackets so that the json file can be reused
        #f_write.seek(0,2)                 # end of file
        #size=f_write.tell()               # the size...
        #f_write.truncate(size-2)          # truncate at that size - how ever many characters
        #f_write.write("]}")
        f_write.close()

import os

for filename in os.listdir("/home/belinda/Desktop/HonoursProject/Project/Data"):
    if filename.endswith(".json") and filename.startswith("tweet"): 
        #print(filename)
        removeDuplicates(filename)
        continue
    else:
        continue


