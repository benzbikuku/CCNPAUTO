
from genie.testbed import load
from pprint import pprint
tb = load('/home/benz/CCNPAUTO/24_pyats_space/pyats_space/pyats_environment/yaml/my_testbed.yaml')
dev = tb.devices['CSR-173']
# dev.connect()
## If the hostname in the yaml file is different
# dev.connect(learn_hostname=True)
# To prevent printing out the device output
dev.connect(log_stdout=False, learn_hostname=True)
# pprint(dir(dev.api))
print(dev.api.get_interface_running_config('GigabitEthernet1'))

sh_ver_parsed = dev.parse("show version")
sh_ip_int_brie = dev.parse("show ip interface brief")
# print(sh_ver_parsed)
print(sh_ver_parsed['version']['xe_version'])
# pprint(sh_ip_int_brie)
int_parsed = sh_ip_int_brie['interface']
# print(int_parsed)
# #
for int in int_parsed:
	print(f" Name: {int} ,  IP: {int_parsed[int]['ip_address']}, Status: {int_parsed[int]['status']}")
#
