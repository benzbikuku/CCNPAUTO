import json
from pprint import pprint
import requests
### Hide insecure Warning
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://192.168.1.95/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet"
# url = "https://192.168.1.95:443/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet"

payload={}
headers = {
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28='
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)
# print(response.text)
# print(dir(response))
# print(type(response))
# print(type(response.text))
# print(type(response.json()))

# t = response.text
# dict_data = json.loads(t)
# print(type(dict_data))
# pprint(dict_data)


dict_data = response.json()
# print(dict_data)
int_list = dict_data['Cisco-IOS-XE-native:GigabitEthernet']
# pprint(int_list)
for intf in int_list:
    try:
        print("GigabitEthernet"+intf['name'], intf['ip']['address']['primary']['address'])
    except KeyError:
        continue
      
# import requests

# url = "https://192.168.1.95/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet"

# payload = {}
# headers = {
#   'Accept': 'application/yang-data+json',
#   'Authorization': 'Basic Y2lzY286Y2lzY28='
# }

# response = requests.request("GET", url, headers=headers, data=payload)

# print(response.text)
