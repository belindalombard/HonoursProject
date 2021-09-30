
totalTweets = 0

import json

def count(filename):
    with open(filename) as data_file:    
        d = json.load(data_file)
        for tweet in d:
            global totalTweets
            totalTweets += 1
import os
filename = "SATweets.json" 
count(filename)
print(totalTweets)
