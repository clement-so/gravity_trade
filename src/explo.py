## 0.A Import libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport

## 0.B Import functions
from utils.custom_functions import generate_descriptive_analysis
def generate_descriptive_analysis(df : pd.DataFrame, output_filename: str) :
    """This function will create a HTML report describing the dataframe submitted.
    Careful, this can be time-consuming.

    Args:
        df (pd.DataFrame): _description_
    """

    # Generate the ProfileReport
    profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)

    # Save the report as an HTML file
    path_to_save = os.path.join(r"./reports", output_filename + ".html")
    profile.to_file(path_to_save)

## O.C Arguments
path_to_data = r'./data'

tweets_filename = r"01.Tweets.csv"
retweets_filename = r"02.Retweets.csv"
users_filename = r"03.Users.csv"

## 1. Import data
users = pd.read_csv(os.path.join(path_to_data,users_filename),
    dtype = {'user_id': 'int64'}
)
users = users.drop(columns=['Unnamed: 0'])

# generate_descriptive_analysis(df = users, output_filename="users_descript") # Comment out 

# Let's have a look
print("Users")
print(users.head())

# a. Top Ten countries represented?
top10_countries = users.profile_location_country_en.value_counts().sort_values()[-10:]

## TWEETS

tweets = pd.read_csv(os.path.join(path_to_data, tweets_filename),
    dtype = {'user_id': 'int64'}
)
tweets = tweets.drop(columns=['Unnamed: 0'])

# generate_descriptive_analysis(df = tweets, output_filename="tweets_descript") # Comment out 

# Let's have a look
print("Tweets")
print(tweets.head())

## RETWEETS
retweets = pd.read_csv(os.path.join(path_to_data, retweets_filename),
    dtype = {'target': 'int64',
    'source': 'int64'}
)
retweets = retweets.drop(columns=['Unnamed: 0'])
generate_descriptive_analysis(df = retweets, output_filename="retweets_descript")
# Let's have a look
print('Retweets')
print(retweets.head())

# I will count the number of received retweets by tweets, and a dummy if it has been done by someone from China or identified as. 
# User_id = The user ID of the retweeter.
reweets = pd.merge(left = retweets, right=users[['user_id','profile_location_country_en']], left_on='target', right_on = 'user_id', how='left')
print(retweets.head())
print(retweets.columns)

# No match, strange. Let's have a look at the ones that are in both. 
