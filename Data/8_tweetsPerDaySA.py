
days = {}

import json

def count(filename):
    d = json.load(filename)
    for tweet in d:
        global days
        date=tweet['time_posted'][0:10]    
        days[date]=days.get(date,0)+1

import os

with open("SATweets.json") as filename:
    count(filename)

print(days)

