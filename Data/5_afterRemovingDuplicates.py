totalTweets = 0

import json

def count(filename):
    with open(filename) as data_file:    
        d = json.load(data_file)
        for tweet in d:
            global totalTweets
            totalTweets += 1
import os

for filename in os.listdir("/home/belinda/Desktop/HonoursProject/Project/Data"):
    if filename.endswith(".json") and filename.startswith("dup"): 
        count(filename)
        continue
    else:
        continue

print(totalTweets)
