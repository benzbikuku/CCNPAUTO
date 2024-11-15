#! /usr/local/Python_envs/Python3/bin/python3

'''3.PUT Change Hostname'''
import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://192.168.0.63/restconf/data/Cisco-IOS-XE-native:native/hostname"

payload = json.dumps(
	{
		"hostname": "From-Python"
	}
)
headers = {
	'Accept': 'application/yang-data+json',
	'Content-Type': 'application/yang-data+json'
}

response = requests.request("PUT", url, headers=headers, data=payload,verify=False,auth=('admin','admin'))

print(response)