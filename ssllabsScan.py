#!/usr/bin/env python

"""Add Docstring"""

import requests
from Models import Info
from pprint import pprint

API = "https://api.ssllabs.com/api/v2/"

def request(path, payload={}):

	"""This is a helper method that takes the path to the relevant
		API call and the user-defined payload and requests the 
		data/server test from Qualys SSL Labs.  

		Returns a Python Object"""

	url = API + path 
	print url
	response = requests.get(url, params=payload)
	print(response.url)
	data = response.json()
	return data

def info():
	
	"""Add Docstring"""

	path = "info"
	data = request(path)
	pprint(data)

	info = Info.Info(data['engineVersion'], data['criteriaVersion'], data['clientMaxAssessments'], data['maxAssessments'], data['currentAssessments'], data['messages'] )
	print info.maxAssessments
	print info.messages

def analyze(host, publish="off", all="done"):
	
	"""Add Docstring"""

	path = "analyze"
	payload = {'host': host, 'publish': publish}
	data = request(path, payload)
	pprint(data)
	#for i in data['endpoints']:
	#	for k, v in i.iteritems():
	#		if k == "grade":
	#			print k,v

def getEndpointData(host, s):
	
	"""Add Docstring"""

	path = "getEndpointData"
	payload = {'host': host, 's': s}
	data = request(path, payload)
	pprint(data)

def test():
	info()

if __name__ == "__main__":
	test()

