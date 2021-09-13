#!/bin/sh

python3 1_getTweetTextFromJson.py
python3 2_PPRemovePunctuation.py

if  ! [ -n "$1"]
then
	echo "Manual Processing"
	python3 3_ManuallyRemoveTweets.py
else
	cp 2_PreprocessedData.txt 3_Tweets.txt
fi	

python3 4_PreprocessingForLDA.py 

