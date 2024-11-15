import json
import requests
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://192.168.1.95:443/restconf/data/Cisco-IOS-XE-native:native/hostname"

################ from dict
# host_dict = {"hostname": "CSR-173_New1"}
# payload = json.dumps(host_dict)

########### send from multiline string
# payload = """{"hostname": "CSR-173_New"}"""

########## from file
with open('/home/benz/CCNPAUTO/22_RESTCONF/host.json') as host:
    payload = host.read()
    
print(payload)

######## user input
# host_input = input("Enter Hostname: ")
# host_dict = {"hostname": host_input}
# payload = json.dumps(host_dict)

headers = {
    'Accept': 'application/yang-data+json',
    'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28='
}

response = requests.request("PUT", url, headers=headers, data=payload, verify=False)

print(response.status_code)
