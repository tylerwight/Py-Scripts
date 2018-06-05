import urllib2
import json
import requests


#A script created to parse a specific frontend to get Virtual machine information. Used to help manage all the VMs.


#repeat 10 times because there are 10 pages to go through
for j in range(1,10):
	#set header with auth token
	headers = {'Accept' : 'application/json', 'Accept_version' : 'v1', 'Authorization' : 'Basic xxxxx<cut>xxxxxxxxxx'}
	#use var j to craft the URL
	url= 'https://blahblah.com/servers?page=' + str(j) + '&per_page=20'
	
	#get response using URL and header above, take response content and put it in variable 'data'
	response = requests.get(url,headers=headers)
	data=response.content
	
	#convert data to json formatting and load into variable stff
	stuff=json.loads(data)
	stuff=response.json()
	#print contents of stuff 
	for i in range(0,len(stuff)):
		#print(i)
		if len(stuff[i]["ip_addresses"]) > 0:
			print(stuff[i]["hostname"] + "/" + stuff[i]["ip_addresses"][0]["address"])
		else:
			print(stuff[i]["name"] + "/ No IP found")
		
