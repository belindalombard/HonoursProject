from collections import Counter

f = open("end_topics.txt", 'w') 

def getTopTenWords(words, T):
    with open("end_topics.txt", 'a') as f: 
        D = {}
        D = Counter(words)
        print(str(T) + ": " + str(D))
        words = D.most_common(10)
        f.write("TOPIC " + str(T)+ '\n') 
        w = []
        for word in words: 
            w.append(word[0])
        f.write(str(w)+'\n')



with open('topics.txt', 'r') as f: 
    lines = f.readlines()
    t = 0
    words = []
    result = []
    for line in lines:
        line = line[line.find('[')+1:line.find(']')]
        #print(line) 
        if (t%10==0 and t>0) or t==(len(lines)-1):
            #print(words)
            getTopTenWords(words, t//10)
            words = []
        for word in line.split(', '):
            words.append(word)
        t+=1
