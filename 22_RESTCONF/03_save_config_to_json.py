import json
from pprint import pprint
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://192.168.1.95/restconf/data/Cisco-IOS-XE-native:native"

headers = {
    'Accept': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28='
}

response = requests.request("GET", url, headers=headers, verify=False)

dict_data = response.json()
print(dict_data)

with open('/home/benz/CCNPAUTO/22_RESTCONF/conf.json', 'w') as conf:
    json.dump(dict_data, conf, indent=4)
