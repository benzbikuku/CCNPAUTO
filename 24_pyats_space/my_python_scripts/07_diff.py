
## Learn
from pprint import pprint
from pyats.topology import loader
import json
tb = loader.load('/home/benz/CCNPAUTO/24_pyats_space/yaml/my_testbed_test.yaml')
dev = tb.devices['CSR-173']
dev.connect(log_stdout=False)
#
# learn_int = dev.learn("interface")
# print(dir(learn_int))
# pprint(learn_int.to_dict())
# print(type(tb.devices.items()))
# print(tb.devices.items())
output1 = {}
for name, dev in tb.devices.items():
	dev.connect()
	output1[name] = {}
	output1[name]['interface'] = dev.learn('interface').to_dict()

pprint(output1)
with open('output2.info', 'w') as data:
	json.dump(output1, data, indent=4)
print(tb.devices)