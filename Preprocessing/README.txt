Files needed (exlcluding your datafile): 
	- usefulFunctions.py
	- 1_getTweetTextFromJson.py
	- 2_PPRemovePunctuation.py

Requirements before doing the steps describes here: 
	- A json file in the format
		{ 'data': [{ ((fields)), 'text' : 'whatever the text', ((more fields))}] } 
	- which contains all the Tweets that you'd like to perform this analysis on. 
	- Call this file OriginalSATweetset.json

STEP 1: 
	- Run the file 1_getTweetTextFromJson.py
	- This will generate two files: 
		1.  1_rawTweetsInReadableFormat.txt which contains the tweets in a format that is readable for manual analysis
		2.  1_rawTweetTextAsList.txt which contains the tweets stored as a list seperated with "#####" that can easily be used by python

STEP 2: Preprocessing - Removing punctuation, accents and special characters
	- Run the file 2_PPRemovePunctuation.py
