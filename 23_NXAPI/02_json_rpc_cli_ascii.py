#! /usr/local/Python_envs/Python3/bin/python3
import requests
import json
from pprint import pprint

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
"""
Modify these please
"""

switchuser='admin'
switchpassword='Kessy,2012'

url='https://192.168.1.96/ins'
myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "int Eth1/5",
      "version": 1
    },
    "id": 1,
    "rollback": "rollback-on-error"
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "descrip from json-rpc 4",
      "version": 1
    },
    "id": 2,
    "rollback": "rollback-on-error"
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "no switch",
      "version": 1
    },
    "id": 3,
    "rollback": "rollback-on-error"
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "ip add 15.15.15.15 255.255.255.0",
      "version": 1
    },
    "id": 4,
    "rollback": "rollback-on-error"
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "no shut",
      "version": 1
    },
    "id": 5,
    "rollback": "rollback-on-error"
  }
]
try:
  response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify=False)
  print(response.status_code)
  if response.status_code!=200:
    raise Exception(f"{response.status_code} \n {response.text}")
  # pprint(response)
  # print(response['result']['msg'])
  output = response.json()

  pprint(output)
  
except Exception as e:
  print(f"Exception occured with {e}")
# print(response['result']['msg'])




