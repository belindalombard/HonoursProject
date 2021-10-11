#PARAMETERS
sep = "#####" #Seperator used


#------------------------------------#


#Converts the string that looks like a list to an actual list type
def stringToList(string):
     return string.split(sep)

def printDataInNiceWay(li):
    k = 1
    for tweet in li: 
        print("Tweet "+str(k)+": "+tweet+'\n')
        k+=1

def getSeperator():
    return sep
