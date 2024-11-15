from ncclient import manager

lab_173 = {'host': '192.168.1.95',
           'port': 830,
           'username': 'cisco',
           'password': 'cisco',
           'hostkey_verify': False,
           'device_params': {'name': 'csr'}}

rtr_mgr = manager.connect(**lab_173)
output = rtr_mgr.get_config('running').data_xml
# print(output)
print(type(output))
with open('/home/benz/CCNPAUTO/21_NETCONF/conf.xml', 'w') as xml_data:
    xml_data.write(output)

rtr_mgr.close_session()