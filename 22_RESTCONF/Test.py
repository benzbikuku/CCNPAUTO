import requests

url = "https://192.168.1.95/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet"

payload = {}
headers = {
  'Accept': 'application/yang-data+json',
  'Authorization': 'Basic Y2lzY286Y2lzY28='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
