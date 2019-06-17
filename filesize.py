#!/usr/bin/python

#imports
import requests
import json

#Main URL for the Meraki Platform
dashboard = "https://(brickftp web address)"
#api token and other data that needs to be uploaded in the header
headers = {'Content-Type': 'application/json'}



#pull back all of the networks for the organization
get_network_url = dashboard + '/api/rest/v1/folders/'

#request the network data
get_network_response = requests.get(get_network_url, headers=headers, auth=HTTPBasicAuth('(Password)', 'x'))

#puts the data into a json format
get_network_json = get_network_response.json()

print(json.dumps(get_network_json, indent=4, separators=(',', ': ')))
