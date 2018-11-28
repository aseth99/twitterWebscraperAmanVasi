import json
import sys
from tweepy import Cursor
from twitter_scraper_client import get_twitter_client

# user = sys.argv[1] #uses first arguement that we enter in command
# client = get_twitter_client()
# fname = "user_timeline_{}.json".format(user)

# with open(fname, 'w') as f:
	# for page in Cursor(client.user_timeline, screen_name=user, count=200).pages(16):
		# for status in page:
			# f.write(json.dumps(status._json)+"\n")


if __name__ == '__main__':
	#testName = sys.argv[1]
	client = get_twitter_client()
	#fname = "home_timeline_{}.json".format(testName)
	# #prints out the x number of tweets at top of timeline
	# for status in Cursor(client.home_timeline).items(100):

	# 	#process single status
	# 	print(status.text)

	#with open('home_timeline.json', 'w') as f: saves a json file, the jsonl files puts each status on one line
	#jsonl file allows file to be split, easier to process one line at a time

	#limits to 800 from our own timeline, 3200 from a specific user 
	with open("home_timeline.json", 'w') as f:
		for page in Cursor(client.home_timeline, count=200).pages(4):
			for status in page:
				f.write(json.dumps(status._json)+"\n")

#this function will simply get tweets from home timeline and print them into command
# if __name__ == '__main__':
# 	client = get_twitter_client()

# 	#prints out the x number of tweets at top of timeline
# 	for status in Cursor(client.home_timeline).items(100):

# 		#process single status
# 		print(status.text)