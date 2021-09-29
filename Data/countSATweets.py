
totalTweets = 0
totalLocation = 0

import json

f = open("SATweets.json", "w")
f.write("{\"data\": [\n")

def count(filename):
    with open(filename) as data_file:    
        d = json.load(data_file)
        for tweet in d['data']:
            location = tweet['location']
            print(location, end=", ")
import os

for filename in os.listdir("/home/belinda/Desktop/HonoursProject/Project/Data"):
    if filename.endswith(".json") and filename.startswith("tweet"): 
        print(totalTweets)
        print(filename)
        
        count(filename)
        continue
    else:
        continue


