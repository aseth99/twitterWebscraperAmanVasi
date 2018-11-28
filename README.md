# twitterWebscraperAmanVasi
How to Gather Tweets into An Excel Sheet: An Introduction

STEPS:

1.
-get a twitter developer account (developer.twitter.com), then export your keys/token into the environment (terminal)
export API_KEY=[redacted]
export API_SECRET_KEY=[redacted]
export ACCESS_TOKEN=[redacted]
export ACCESS_TOKEN_SECRET=[redacted]

2.
-running twitter_get_home_timeline.py will get you the last 800 tweets from your home timeline

3.
-running get_user_timeline.py will ask you for twitter accounts to scrape (gets last 3200 tweets)
will keep asking until you type done

-after running above function you will have separate json files with the tweets from each account you requested

4a. Unfiltered
-running all_json_to_csv.py will ask you to name the .csv file

-then it prompt you for which twitter accounts tweets you want in csv format (assuming you already did step 3 with their account, and have the json file associated with the account)

-will load all specified usernames into a csv file

4b. Filtered
-running filter_json_to_csv.py will ask you to name the .csv file

-then it will ask you for words you want to filter the tweets by (only tweets containing at least one of the words will be selected)

-then it will prompt you for which twitter accounts tweets you want in csv format (assuming you already did step 3 with their account)

5. 
-you have a .csv file!
