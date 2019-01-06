from randomString import getRandomString
import requests
from pprint import pprint
from time import sleep
import json
ApiKey = 'apikey'

#ask yt if it's a genuine link and loop while doing it
while True:
	videoId = getRandomString(11,'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') #"uQbR6wCRVs8"
	print("Generated random YouTube ID:")
	print (videoId)
	sleep(0.5)
	
	url = f'https://www.googleapis.com/youtube/v3/videos?id={videoId}&key={ApiKey}&part=status'
	url_get = requests.get(url)
	print ("Finished YouTube query through API v3.")
	sleep(0.5)
	#pprint(url_get.json())
	responseString = (url_get.json())
	#print(json.dumps(responseString))
	print ("Data collected.")
	sleep(0.5)
	#print(type(responseString))
	responseString = json.dumps(responseString)
	#print(type(responseString))
	print ("Converted from data to string.")
	sleep(0.5)
	#print(responseString)
	print ("Evaluating...")
	sleep(0.5)
	print("...")
	sleep(2.5)
	if "publicStatsViewable" not in responseString:
			print("Video ID does not exist. Restarting after a 5 minute wait due to query limits.")
			sleep(300)
	if "publicStatsViewable" in responseString:
		sleep(0.5)
		print("Actual live video found.")
		print (videoId)
		break


#if link genuine, add to data document

#loop forever but with 5 minute pause as a server utility
