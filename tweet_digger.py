#! /usr/bin/env python
# script to import tweet history via twitter's timeline pagination
import urllib
import simplejson

user  = raw_input("User's screen name please: ")
count = 100 # best result 
pages = range(3200/count); #Twitter allows retrieving only the last 3200 tweets
f = open(user + '.txt', 'w')

min_id = None
for page in pages:
    queryUrl = 'https://api.twitter.com/1/statuses/user_timeline.json?' + 'screen_name=' + user + '&count=' + str(count) + '&include_rts=1'
    if min_id:
        # Get the maximum id to be retrieved - which is one less than the minimum of the previous page
        max_id    = min_id + 1
        queryUrl = queryUrl + '&max_id=' + str(max_id)

    result = simplejson.load(urllib.urlopen(queryUrl))
    min_id = None
    for tweet in result:
        f.write('At ' + tweet['created_at'] + ':\n' + tweet['text'].encode('utf-8') + '\n\n');
        min_id =  tweet['id'] if (tweet['id'] < min_id or (not min_id)) else min_id;
    
f.close();

