### Tweet Collection Script 

### Importing required packages 
import os 
import tweepy
from dotenv import load_dotenv

load_dotenv()
### Getting the API key from the .env file 
API_KEY = os.getenv("TWITTER_BEARER_TOKEN", default = "NOT AUTHORIZED")

### Establishing the tweepy client 
Client = tweepy.Client(bearer_token = API_KEY)
query = "#COP26 lang:en"

### Class definition 
class tweet_collector :
    def __init__(self, query, Client, START_DATE, END_DATE, MAX_RESULTS) :
        self.Client = Client
        self.query = query 
        self.start = START_DATE
        self.end = END_DATE
        self.max_results = MAX_RESULTS

    def collection_job(self) :
        pass


