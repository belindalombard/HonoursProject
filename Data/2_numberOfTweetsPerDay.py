
days = {}

import json

def count(filename):
    with open(filename) as data_file:    
        d = json.load(data_file)
        for tweet in d['data']:
            global days
            date=tweet['time_posted'][0:10]    
            days[date]=days.get(date,0)+1

import os

for filename in os.listdir("/home/belinda/Desktop/HonoursProject/Project/Data"):
    if filename.endswith(".json") and filename.startswith("tweet"): 
        #print(filename)
        count(filename)
        continue
    else:
        continue

#count('SATweets.json')

print(days)

