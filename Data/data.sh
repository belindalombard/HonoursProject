#!/bin/bash

echo "OUTPUT FILE" > output.txt
echo "" >> output.txt
echo "Total number of tweets collected is: " >> output.txt
python3 1_countNumberOfTweets.py >> output.txt
echo "" >> output.txt
echo "Tweets posted per day: " >> output.txt
python3 2_numberOfTweetsPerDay.py >> output.txt
echo "" >>output.txt 
echo "Proportion of tweets with location tags: " >> output.txt
python3 3_countLocationTags.py >> output.txt

