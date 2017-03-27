import urllib2
import json
from sets import Set
import pickle

url = "https://www.twitter.com/{}/followers/users?include_available_features=1&include_entities=1&max_position={}&reset_error_state=false"
accounts  = open("Personality link.txt", "r")


for line in accounts:

	words=line.split(' ')
	account=words[1][:-1]
	file_name=words[0][:-1] + ".obj"
	next_position = -1
	followers = Set()

 	filehandler = open(file_name, "w")

 	print "[fetching]...{}".format(account)

	while True:
		url2 = url.format(account, next_position)
		print url2
		req = urllib2.Request(url2)
		req.add_header('Referer', 'https://www.twitter.com/amaneureka/followers')
		req.add_header('Cookie', 'guest_id=v1%3A146740672877282706; kdt=YmfRDJq1J0U1NToWQkHImW7gabE0iy9X6hv5dFds; remember_checked_on=1; twid="u=1454346458"; auth_token=6d64082c4badc918178a4375ef457122556c61dd; ct0=44495cab3dfe2a0eda16fc4171dc8ced; moments_profile_moments_nav_tooltip_self=true; lang=en; moments_moment_guide_create_moment_tooltip=true; moments_profile_moments_nav_tooltip_other=true; eu_cn=1; __utma=43838368.1809007874.1467462848.1489247956.1490364856.2; __utmc=43838368; __utmz=43838368.1489247956.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); SSESS3c8b2bbd5af1180dab341c61a9900084=sqk6vcl56n4cmku8rust1puks7; lang=en; has_js=1; external_referer="padhuUp37zjgzgv1mFWxJzx4vPNPpMnZ52M34anUtp0=|0"; _ga=GA1.2.1809007874.1467462848; _gat=1; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCEVezN5YAToMY3NyZl9p%250AZCIlMTYxYjAxODAzNmJmZDJlMGNhYjNkYmQ1ZDkwODMxMzI6B2lkIiU4NDFm%250ANjdlMDNmZmNhYzNhZGRkMjBlNWNlNTA2MzMwOA%253D%253D--9dff20c821da6b41091c4b7b36c32dcb6b93eae1')

		resp = urllib2.urlopen(req)
		content = resp.read()

		index = -1
		try:
			while True:
				index = index + 1
				index = content.index('data-screen-name', index)
				index2 = content.index('\\"', index + 20)
				followers.add(content[index + 19: index2])
		except:
			pass

		j = json.loads(content)
		if j['has_more_items'] == True:
			next_position = j['min_position']
		else:
			break

	pickle.dump(followers, filehandler) 
	# len(followers)
	# print followers