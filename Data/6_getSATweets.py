
import json

f = open("SATweets.json", "w")

json_entries = []

def getSATweets(filename):
    with open(filename) as data_file:    
        d = json.load(data_file)
        for tweet in d:
            #print(tweet)
            location = tweet['location']
            if "south africa" in location.lower():
                global totalLocation
                json_entries.append(tweet)

import os

for filename in os.listdir("/home/belinda/Desktop/HonoursProject/Project/Data"):
    if filename.endswith(".json") and filename.startswith("dup"): 
        #print(filename)
        getSATweets(filename)
        continue
    else:
        continue

json.dump(json_entries, f)
f.close()
