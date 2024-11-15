#! /usr/local/Python_envs/Python3/bin/python3

import requests
import json
from pprint import pprint

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
      "cmd": "show hardware ",
      "version": 1
    },
    "id": 1
  }
]
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify=False).json()
# print(response)
# print(type(response))
# print(dir(response))
# pprint(response['result']['body'])
pprint(response['result']['body']['kickstart_ver_str'])









# import requests
# import json
# from pprint import pprint

# from requests.packages.urllib3.exceptions import InsecureRequestWarning
# requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
# """
# Modify these please
# """

# switchuser='admin'
# switchpassword='admin'

# url='https://192.168.0.201/ins'
# myheaders={'content-type':'application/json-rpc'}
# payload=[
#   {
#     "jsonrpc": "2.0",
#     "method": "cli",
#     "params": {
#       "cmd": "show hardware",
#       "version": 1
#     },
#     "id": 10
#   }
# ]

# response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify=False).json()

# pprint(response)
# print(response['result']['body']['kickstart_ver_str'])
# print(response['result']['body']['kick_file_name'])


# # 