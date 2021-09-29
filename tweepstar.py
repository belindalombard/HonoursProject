import os
import pandas as pd
import tweepy
import json
import csv
import re
from textblob import TextBlob
import string
import preprocessor as p
import os
import time
import datetime
import getpass
import sys

auth = tweepy.OAuthHandler('LSZgNrncrRNPPMG72jQMNnBko','K46gL3qnACRcOBRM95p7Zk9nXlKbsjdV3mJaLhLYdHo4VfBfTL')

auth.set_access_token('891601069595398144-GjJ3j5E24vcUQKkgnbOIQ30j8jmtObZ','QiQAAcptrY7zrSnLq4crUtSPdgRdNC0zxY9bJbT4QOWKR')

api= tweepy.API(auth)

try:
    api.verify_credentials()
    print("Auth okay")
except:
    print("Error during Auth")

#os.chdir('C:\\Users\\' + getpass.getuser() +'\\Documents\\tweetcollector')



def scraptweets(search_words, date_since, numTweets, numRuns, filename_end):
    
    # Define a for-loop to generate tweets at regular intervals
    # We cannot make large API call in one go. Hence, let's try T times
    
    # Define a pandas dataframe to store the date:

    db_tweets = pd.DataFrame(columns=['username','acctdesc','location','following','followers','totaltweets','usercreatedts','tweetcreatedts','retweet_count','text', 'favorite_count', 'possible_sensitive', 'filter_level', 'lang', 'hashtags', 'time_posted', 'tweet_id', 'in_reply_to_status_id', 'in_reply_to_user_id', 'coordinates', 'place', 'truncated', 'quoted_status_id', 'quoted_status_text', 'quoted_status_user_id', 'quoted_status_user_name' ,'matching_rules', 'withheld_copyright', 'withheld_in_countries', 'withheld_scope', 'scopes'])
                       
    program_start = time.time()
    
    for i in range(0, numRuns):
            # We will time how long it takes to scrape tweets for each run:
            start_run = time.time()
            # Collect tweets using the Cursor object
            # .Cursor() returns an object that you can iterate or loop over to access the data collected.
            # Each item in the iterator has various attributes that you can access to get information about each tweet
            api=tweepy.API(auth,wait_on_rate_limit=True)

            data = api.rate_limit_status()
            print(data['resources']['statuses']['/statuses/home_timeline'])
            print(data['resources']['users']['/users/lookup'])
            print(data['resources'])
            tweets = tweepy.Cursor(api.search, geocode="33.9249,18.4241,2400km", q = search_words, since = date_since, tweet_mode = 'extended',lang='en').items(numTweets)
            # Store these tweets into a python list
           # try: 
            tweet_list  = [tweet for tweet in tweets]
           # except tweepy.error.TweepError:
           #     print(sys.exc_info())
           #     to_csv_timestamp = datetime.date.today().strftime('%Y%m%d_%H%M%S')
           #     path = os.getcwd()
           #     filename_json = path + '\\data\\' + to_csv_timestamp + filename_end + '_incomplete.json'
           #     db_tweets.to_json(filename_json, orient = 'table')
           #     program_end = time.time()
           #     print('Scraping has not completed!')
           #     print('completed unfil run :' + str(i))
           #     print('error obtained at '+ time.asctime())
   

            # Obtain the following info (methods to call them out):
            # user.screen_name - twitter handle
            # user.description - description of account
            # user.location - where is he tweeting from
            # user.friends_count - no. of other users that user is following (following)
            # user.followers_count - no. of other users who are following this user (followers)
            # user.statuses_count - total tweets by user
            # user.created_at - when the user account was created
            # created_at - when the tweet was created
            # retweet_count - no. of retweets
            # (deprecated) user.favourites_count - probably total no. of tweets that is favourited by user
            # retweeted_status.full_text - full text of the tweet
            # tweet.entities['hashtags'] - hashtags in the tweet
            # Begin scraping the tweets individually:

            noTweets = 0
            
            for tweet in tweet_list:
                try:
                    username = tweet.user.screen_name
                    user_id = tweet.user.id
                    acctdesc = tweet.user.description
                    location = tweet.user.location
                    following = tweet.user.friends_count
                    followers = tweet.user.followers_count
                    totaltweets = tweet.user.statuses_count
                    usercreatedts = tweet.user.created_at
                    tweetcreatedts = tweet.created_at
                    retweet_count = tweet.retweet_count
#                quote_count = tweet.quote_count
#                reply_count = tweet.reply_count
                    try:
                        favorite_count = tweet.favorite_count
                    except AttributeError:
                        favorite_count = None
                

                    try:
                        possible_sensitive = tweet.possibly_sensitive
                    except AttributeError:
                        possible_sensitive = None
                    
                    try:
                        filter_level = tweet.filter_level
                    except AttributeError:
                        filter_level = None
                    try:
                        lang = tweet.lang
                    except AttributeError:
                        lang = None

                    hashtags = tweet.entities['hashtags']
                
                    time_posted = tweet.created_at
                    tweet_id = tweet.id
                    try:
                        in_reply_to_status_id = tweet.in_reply_to_status_id
                    except AttributeError:
                        in_reply_to_status_id = None
                    try:
                        in_reply_to_user_id = tweet.in_reply_to_user_id      
                    except AttributeError:
                        in_reply_to_user_id = None
                    try:
                        in_reply_to_screen_name = tweet.in_reply_to_screen_name
                    except AttributeError:
                        in_reply_to_screen_name = None
                    try:
                        coordinates = tweet.coordinates
                    except AttributeError:
                        coordinates = None
                    try:
                        place = tweet.place
                    except AttributeError:
                        place = None

                    truncated = tweet.truncated
                
                    if tweet.is_quote_status:
                        try:
                            quoted_status_id = tweet.quoted_status.id
                            quoted_status_text = tweet.quoted_status.text
                            quoted_status_user_id = tweet.quoted_status.user.id
                            quoted_status_user_name = tweet.quoted_status.user.screen_name
                        except AttributeError:
                            quoted_status_id = None
                            quoted_status_text = None
                            quoted_status_user_id = None
                            quoted_status_user_name = None
                    else: 
                        quoted_status_id = None
                        quoted_status_text = None
                        quoted_status_user_id = None
                        quoted_status_user_name = None
                

                    try:
                        matching_rules = tweet.matching_rules
                    except AttributeError:
                        matching_rules = None

                    try:
                        withheld_copyright = tweet.withheld_copyright
                    except AttributeError:
                        withheld_copyright = None
                    try:
                        withheld_in_countries = tweet.withheld_in_countries
                    except AttributeError:
                        withheld_in_countries = None
                    try:
                        withheld_scope = tweet.withheld_scope
                    except AttributeError:
                        withheld_scope = None
                    try:
                        scopes = tweet.scopes
                    except AttributeError:
                        scopes = None 

                              

#               expanded_url = tweet.entities.urls['expanded_url']
#               lang = tweet.metadata['iso_language_code']
#               geo = tweet.geo
#               possibly_sensitive = tweet.possibly_sensitive



                    try:
                        text = tweet.retweeted_status.full_text
                    except AttributeError: #Not a Retweet`
                        text = tweet.full_text
                # Add the 11 variables to the empty list - ith_tweet:

                    ith_tweet = [username, acctdesc, location, following, followers, totaltweets, usercreatedts, tweetcreatedts, retweet_count, text, favorite_count, possible_sensitive, filter_level, lang, hashtags, time_posted, tweet_id, in_reply_to_status_id, in_reply_to_user_id, coordinates, place, truncated, quoted_status_id, quoted_status_text, quoted_status_user_id, quoted_status_user_name ,matching_rules, withheld_copyright, withheld_in_countries, withheld_scope, scopes]
                # Append to dataframe - db_tweets
                    db_tweets.loc[len(db_tweets)] = ith_tweet
                
                    noTweets += 1
                except KeyboardInterrupt:
                    to_csv_timestamp = datetime.date.today().strftime('%Y%m%d_%H%M%S')
                    path = os.getcwd()
                    filename_json = path + '\\data\\' + to_csv_timestamp + filename_end + '_interrupted' + '.json'
                    db_tweets.to_json(filename_json, orient = 'table')
                    program_end = time.time()
                    print('Scraping has been interrupted!')
                    print('Total time spent scraping is {} minutes'.format(round(program_end - program_start)/60,2))
                    print(path)
                    print(filename_json)

            #Run ended:
            end_run = time.time()
            duration_run = round((end_run-start_run)/60,2)
            print('no. of tweets scrape for run {} is {}'.format(i+1, noTweets))
            print('time taken for {} run to complete is {} mins'.format(i+1, duration_run))
            print('finished at: ' + time.asctime())           
            time.sleep(1000)
        
                # Once all runs have completed, save them to a single csv file

    to_csv_timestamp = datetime.date.today().strftime('%Y%m%d_%H%M%S')
    path = os.getcwd()
    filename_json = path + '\\data\\' + to_csv_timestamp + filename_end + '.json'
#    db_tweets.to_csv(filename_csv, index = False)
    db_tweets.to_json(filename_json, orient = 'table')
    program_end = time.time()
    print('Scraping has completed!')
    print('Total time taken to scrape is {} minutes'.format(round(program_end - program_start)/60,2))
    print(program_end)
    print(os.getcwd())
    print(filename_json)


search_words = "#vaccine OR vaccine OR vaccinate OR vaccination OR vaccinated"
#lang = "eng"
date_since = datetime.date.today() - datetime.timedelta(days=6)
date_since = date_since.strftime('%Y-%m-%d')
print('Looking for tweets about '+ search_words  + 'since: ' + date_since)
print('Starting at: ' + time.asctime())
numTweets = 2500
numRuns = 40

scraptweets(search_words,date_since,numTweets,numRuns, filename_end = 'vaccine_tweets')

search_words = 'corona OR COVID OR SARS-cov-2 OR coronavirus OR quarantine OR self-isolation OR pandemic OR lockdown OR SouthAfricaLockdown'
print('Looking for tweets about '+ search_words  + 'since: ' + date_since)
print('Starting at: ' + time.asctime())
date_since = datetime.date.today() - datetime.timedelta(days=6)
date_since = date_since.strftime('%Y-%m-%d')
numTweets = 2000
numRuns = 30

scraptweets(search_words,date_since,numTweets,numRuns, filename_end = 'covidSA')

