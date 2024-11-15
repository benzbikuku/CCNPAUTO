#! /usr/local/Python_envs/Python3/bin/python3
# import requests
# import json

# url = "https://192.168.0.201/ins"

# payload = json.dumps({
#   "ins_api": {
#     "version": "1.0",
#     "type": "bash",
#     "chunk": "0",
#     "sid": "sid",
#     "input": "cat /etc/os-release",
#     "output_format": "json"
#   }
# })
# headers = {
#   'Content-Type': 'application/json',
#   'Authorization': 'Basic YWRtaW46YWRtaW4=',
# }

# response = requests.request("POST", url, headers=headers, data=payload, verify=False)

# print(response.text)

import requests
import json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://192.168.1.96/ins"

payload = json.dumps({
  "ins_api": {
    "version": "1.0",
    "type": "bash",
    "chunk": "0",
    "sid": "1",
    "input": "cat /proc/cpuinfo",
    "output_format": "json"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46S2Vzc3ksMjAxMg==',
  'Cookie': 'nxapi_auth=admin:iEze8XjSVZpc0+D02JDhxSHJddQ='
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)
