
#Returns dictionary with the number of times each word occurs 
def getDictionary(data):
    d = {}
    for tweet in data: 
        for word in tweet: 
            if word in d: 
                d[word] = d[word]+1
            else:
                d[word] = 1
    return d 



def numberOfWords(dictionary):
    total = 0
    for key,value in dictionary.items():
        total += value

    return total

def writeData(tweets, filename):
    f = open(filename, "w")
    add = []
    for t in tweets: 
        add.append("|".join(t))
    f.write("#####".join(add))
    f.close()

def getData(filename):
    with open(filename, 'r') as f:
       s = f.readlines() 
       tweets = str(s).split("#####")
       data = []
       for tweet in tweets: 
            data.append(tweet.split("|"))
       return data


