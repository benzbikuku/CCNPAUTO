from ncclient import manager

router = {
   "host":"ios-xe-mgmt-latest.cisco.com",
   "port":"10000",
   "username":"developer",
   "password":"C1sco12345"

}

with manager.connect(**router, hostkey_verify=False ) as m:
    for capability in m.server_capabilities:
        print('*' * 25)
        print('')
        print(capability)
