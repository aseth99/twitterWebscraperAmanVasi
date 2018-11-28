import json
import csv

#this only works if JSON file is already scraped & saved as user_timeline_[twitterhandle] 

#code from https://stats.seandolinar.com/collecting-twitter-data-converting-twitter-json-to-csv-ascii/
#and used https://stackoverflow.com/questions/21058935/python-json-loads-shows-valueerror-extra-data
 

chooseName = input("\nWhat should we name the csv file?\n\n\n")
csvFileName = "{}.csv".format(chooseName)
csv_out = open(csvFileName, mode='w') #opens csv file
writer = csv.writer(csv_out) #create the csv writer object

fields = ['Twitter Handle & User Name', 'Tweet', ' external URL', 'Hashtags', 'Filter Words', 'Date of Tweet', 'Followers', 'Following', 'RT', 'FAV'] #field names
writer.writerow(fields) #writes field

tweets = []
filterArray = []

exitClause = "notdone"
print("what words do we want to filter by? (already filtering by resilien,adversity,disaster or terrorist)\n\n\n")

while exitClause != "done":
    exitClause = input("(type done if finished)\n\n")
    if exitClause == "done":
    	break
    filterWord = "{}".format(exitClause)
    filterArray.append(filterWord)

if exitClause == "done":
    print("okay... now...")



exitClause = "notdone"
print("(this only works if JSON file is already scraped & saved as user_timeline_[twitterhandle])\n So whose tweets are we outputting to csv?\n\n\n")

while exitClause != "done":
    exitClause = input("(type done if finished)\n\n@")
    if exitClause == "done":
    	break
    jsonFileToBeOpened = "user_timeline_{}.json".format(exitClause)
    for line in open(jsonFileToBeOpened, 'r'):
        tweets.append(json.loads(line))

if exitClause == "done":
    print("converting...")

for line in tweets:
 	
    urlvar = line.get('entities').get('urls')
    if(urlvar):
    	urlvar = urlvar[0].get('expanded_url')
    else:
    	urlvar = "no external urls in this tweet"

    hashtagsVar = line.get('entities').get('hashtags')
    tempHashList = []
    if not hashtagsVar:
    	hashtagsVar = "no hashtags in this tweet"
    else:
    	for i in hashtagsVar:
    		tempHashList.append(i['text'])
    	hashtagsVar = tempHashList



    #writes a row and gets the fields from the (now pyton) dict
    #screen_name and followers/friends are found on the second level hence two get methods
    #filters and only puts tweets in csv that have the word "win" in tweets
    
    if any(x in line.get('text') for x in filterArray):

	    writer.writerow([line.get('user').get('screen_name')+" , "+line.get('user').get('name'),
	                     line.get('text').encode('unicode_escape'), #unicode escape to fix emoji issue
	                     urlvar,
	                     hashtagsVar,
                         filterArray,
	                     line.get('created_at'),
	                     line.get('user').get('followers_count'),
	                     line.get('user').get('friends_count'),
	                     line.get('retweet_count'),
	                     line.get('favorite_count')])
	 
csv_out.close()
