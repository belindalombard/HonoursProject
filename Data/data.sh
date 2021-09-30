#!/bin/bash

start=$(date +%s.%N) 

echo "OUTPUT FILE" > output.txt
echo "" >> output.txt

echo "COUNTING NUMBER OF TWEETS" 
echo "Total number of tweets collected is: " >> output.txt
python3 1_countNumberOfTweets.py >> output.txt
echo "" >> output.txt


echo "COUNTING NUMBER OF TWEETS PER DAY" 
echo "Tweets posted per day: " >> output.txt
python3 2_numberOfTweetsPerDay.py >> output.txt

echo "COUNTING PROPORTION OF TWEETS WITH LOCATION TAGS" 
echo "" >>output.txt 
echo "Proportion of tweets with location tags: " >> output.txt
python3 3_countLocationTags.py >> output.txt
echo "" >> output.txt

echo "REMOVING DUPLICATES" 
python3 4_removeDuplicates.py >> output.txt
echo "" >> output.txt

echo "COUNTING NUMBER OF TWEETS AFTER REMOVING DUPLICATES" 
echo "Number of tweets after removing duplicates: " >> output.txt
python3 5_afterRemovingDuplicates.py >> output.txt

echo "GETTING TWEETS WHERE LOCATION TAG INCLUDES SOUTH AFRICA" 
python3 6_getSATweets.py >> output.txt

echo "" >> output.txt
echo "GETTING NUMBER OF TWEETS IN SOUTH AFRICA" 
echo "Number of tweets with South Africa in location: " >> output.txt
python3 7_countNumberOfSATWeets.py >> output.txt

echo "" >> output.txt
echo "COUNTING NUMBER OF TWEETS PER DAY IN SOUTH AFRICA" 
echo "Number of tweets per day in South Africa: " >> output.txt
python3 8_tweetsPerDaySA.py >> output.txt

echo "" >> output.txt
echo "COPYING FILE TO PREPROCESSING FOLDER" 
cp SATweets.json ../Preprocessing/data.json

duration=$(echo "$(date +%s.%N) - $start" | bc)



echo "Duration: $duration"
