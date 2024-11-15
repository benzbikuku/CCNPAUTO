from ncclient import manager

lab_173 = {'host': '192.168.1.95',
           'port': 830,
           'username': 'cisco',
           'password': 'cisco',
           'hostkey_verify': False,
           'device_params': {'name': 'csr'}}

rtr_mgr = manager.connect(**lab_173)
hostname_filter = '''
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname/>
      </native>
    </filter>
'''

output = rtr_mgr.get_config('running', hostname_filter)
print(output)


rtr_mgr.close_session()