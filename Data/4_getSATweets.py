totalTweets = 0
totalLocation = 0

import json

f = open("SATweets.json", "w")
f.write("{\"data\": [\n")

def getSATweets(filename):
    with open(filename) as data_file:    
        d = json.load(data_file)
        for tweet in d['data']:
            global totalTweets
            totalTweets+=1
            location = tweet['location']
            if "South Africa" in location:
                global totalLocation
                totalLocation += 1
                json.dump(tweet,f)
                f.write(",\n")

import os

for filename in os.listdir("/home/belinda/Desktop/HonoursProject/Project/Data"):
    if filename.endswith(".json") and filename.startswith("tweet"): 
        print(filename)
        getSATweets(filename)
        continue
    else:
        continue
print(totalLocation)
print(totalTweets)
f.write("]}")
f.close()
