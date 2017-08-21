import tweepy
from textblob import TextBlob
import csv

consumer_key = 'zeJkKxOLRkoEeP3wVfFKihsu2'
consumer_secret = 'ZAFsiycyJZ6oYYsOGhtOS7W3uo2Y1cGTywXLWQLnglkcCILhxh'

access_token = '101080126-28FablsmOP9ZqI7mmV3Dw48YV9DPRLyZHmNsF3sr'
access_token_secret = '00tNVt1fGkV0RwwMosgE0R3MUJQWmrMrYrzd0uZlc7lVc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

with open('trump_sentiment_analysis.csv', 'w',newline='\n') as f:
        fieldnames = ['Tweet', 'Sentiment','Polarity','Subjectivity']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for tweet in public_tweets:
            analysis = TextBlob(tweet.text)
            polarity_text = 'Positive'
            if(analysis.sentiment.polarity < 0):
                polarity_text = 'Negative'
            writer.writerow({fieldnames[0]:tweet.text, fieldnames[1]:polarity_text, fieldnames[2]:analysis.polarity, fieldnames[3]:analysis.subjectivity})