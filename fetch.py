# -*- coding: utf-8 -*-
# @Author: Aman Priyadarshi
# @Date:   2017-03-24 20:47:56
# @Last Modified by:   Aastha Gupta
# @Last Modified time: 2017-03-24 23:02:46

import time
import tweepy
from sets import Set
import os.path

limit_fetch = 100
seed_profile = ''
output_file = 'twitter-main.dataset'

# don't push code with your keys!!
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

counter = 0
profiles = [seed_profile]
completed_list = Set()
while counter < limit_fetch and counter < len(profiles):
	current_user = profiles[counter]
	output_file = 'Datasets/{}.dataset'.format(current_user)
	completed_list.add(current_user)
	followers = tweepy.Cursor(api.followers, screen_name=current_user).items()
	print "fetching followers of @{}".format(current_user)
	if not os.path.exists(output_file):
		with open(output_file, "a") as file:
			while True:
				try:
					user = next(followers)
				except tweepy.TweepError:
					time.sleep(60*15)
					user = next(followers)
				except StopIteration:
					break
				file.write("{}\n".format(user.screen_name))
				if (user.screen_name not in completed_list) and (len(profiles) < limit_fetch and user.followers_count < 1000):
					profiles.append(user.screen_name)
	counter = counter + 1