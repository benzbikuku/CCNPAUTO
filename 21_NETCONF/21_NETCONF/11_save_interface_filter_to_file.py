from ncclient import manager
import xml.dom.minidom as md

lab_173 = {'host': '192.168.1.95',
           'port': 830,
           'username': 'cisco',
           'password': 'cisco',
           'hostkey_verify': False,
           'device_params': {'name': 'csr'}}

rtr_mgr = manager.connect(**lab_173)
interface_filter = '''
    <filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
      <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface/>
      </native>
    </filter>
'''

output = rtr_mgr.get_config('running', interface_filter)
xmldata = md.parseString(str(output))
new_data = xmldata.toprettyxml(indent="  ")
print(new_data)
with open('/home/benz/CCNPAUTO/21_NETCONF/21_NETCONF/all_int.xml', 'w') as data:
    data.write(new_data)


rtr_mgr.close_session()