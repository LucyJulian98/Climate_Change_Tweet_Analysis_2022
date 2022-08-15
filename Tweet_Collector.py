### Tweet Collection Script 

### Importing required packages 
import os 
import argparse 
import tweepy
from dotenv import load_dotenv
from datetime import datetime 

load_dotenv()
### Getting the API key from the .env file 
API_KEY = os.getenv("TWITTER_BEARER_TOKEN", default = "NOT AUTHORIZED")

### Setting the other variables as environment variables (explore Argparse)
#query = os.getenv("QUERY", default = "#COP26 lang:en")
#START_DATE = os.getenv("START_DATE", default = "2021-11-01") ## Default start 1 Nov, 2021
#END_DATE = os.getenv("END_DATE", "2021-12-01")  ## Default end 1 Dec, 2021
#MAX_RESULTS = os.getenv("MAX_RESULTS", default = 100)
#PAGE_LIMIT = os.getenv("PAGE_LIMIT", default = 2)

MAX_RESULTS = 100 

### Establishing the tweepy client 
Client = tweepy.Client(bearer_token = API_KEY)

### Reading in user inputs through CLI 
def read_user_CLI() :
    """
    Function to handle the CLI user interactions

    Returns :
    ~~~~~~~~~
    argparse.Namespace : Populated Namespace object

    """
    parser = argparse.ArgumentParser(description = "Takes in user arguments for tweet collection job ")

    ### Adding in the arguments 
    parser.add_argument("query", nargs = '+', type = str, help = "Enter the tweet query.")
    parser.add_argument("start_date", nargs = '+', type = str, help = "Enter the start date.")
    parser.add_argument("end_date", nargs = '+', type = str, help = "Enter the end date.")
    parser.add_argument("page_limit", type = int, help = "Enter the number of pages.")
    parser.add_argument("-q", action = "store_true", help = "Use default value of query.")
    parser.add_argument("-s", action = "store_true", help = "Use default value of start date.")
    parser.add_argument("-e", action = "store_true", help = "Use default value of end date.")
    parser.add_argument("-p", action  = "store_true", help = "Use the default value of page limit.")
    
    return parser.parse_args()



### Class definition 
class tweet_collector :
    def __init__(self, query, Client, START_DATE, END_DATE, MAX_RESULTS, PAGE_LIMIT, STORAGE) :
        self.Client = Client
        self.query = query 
        self.start = START_DATE
        self.end = END_DATE
        self.max_results = MAX_RESULTS
        self.page_limit = PAGE_LIMIT 
        self.storage = STORAGE 

    def collection_job(self) :
        pass


if __name__ == "__main__" : 
    user_args = read_user_CLI()
    print(user_args.query)