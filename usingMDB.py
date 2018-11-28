import pymongo
from pymongo import MongoClient


client = MongoClient()
db = client.oilersTest

posts = db.posts

post_data = {"created_at": "Wed Nov 28 05:45:09 +0000 2018", "text": "RT @Robin_Brownlee: How is the official supposed to see white ice between the back of the goal line and the front of the puck when he has h\u2026","name": "Lowetide", "screen_name": "Lowetide"}
result = posts.insert_one(post_data)

tweet1 = {"created_at": "Wed Nov 28 04:55:37 +0000 2018", "text": "In Sweden, \"shiddhay\" means not quite right, a little off. It's pronounced much like the musical artist Sade pronou\u2026 https://t.co/I6euROYPES", "name": "Lowetide", "screen_name": "Lowetide"}
tweet2 = {"created_at": "Wed Nov 28 04:05:43 +0000 2018", "text": "RT @TPS_Guy: Trey Fix-Wolanksy has 195 career points as an @EdmOilKings, that's 6th all-time for the franchise (current edition). When he h\u2026", "name": "Lowetide", "screen_name": "Lowetide"}
tweet3 = {"created_at": "Wed Nov 28 03:35:26 +0000 2018", "text": "@revRecluse Browns fans deserve a long, long run of success. Playoffs next year!","name": "Lowetide", "screen_name": "Lowetide"}

new_result = posts.insert_many([tweet1, tweet2, tweet3])


print('One post: {0}'.format(result.inserted_id))

print('Multiple posts: {0}'.format(new_result.inserted_ids))

lowetides_post = posts.find_one({'name': 'Lowetide'})
print(lowetides_post)


