
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

def getTopWords(numbers, n): #Returns a list of size n containing the top 5 indexes of a given array
    top_n_array = []
    for i in range(len(numbers)):
        p = numbers[i]
        if p not in top_n_array: 
            if len(top_n_array)<n:
                top_n_array.append(p)
            else:
                minimum = min(top_n_array)
                if p>minimum: 
                    top_n_array[top_n_array.index(minimum)] = p
    return top_n_array
