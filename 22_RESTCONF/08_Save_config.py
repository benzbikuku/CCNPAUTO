import json
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://192.168.0.63/restconf/operations/cisco-ia:save-config/"


headers = {
      'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response = requests.request("POST", url, headers=headers, verify=False)

print(response.text)
print(response.status_code)

