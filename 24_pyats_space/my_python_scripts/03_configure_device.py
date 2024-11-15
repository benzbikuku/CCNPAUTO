

from pyats.topology import loader
from pprint import pprint
tb = loader.load('/home/benz/CCNPAUTO/24_pyats_space/yaml/my_testbed_test.yaml')
dev = tb.devices['CSR-173']
dev.connect()

pre_learn = dev.learn('static_routing')
dev.configure('ip route 1.1.1.100 255.255.255.255 gi1\nip route 1.1.1.101 255.255.255.255 gi1')
post_learn = dev.learn('static_routing')

print("\n\n Pre learned Routes")
pprint(pre_learn.to_dict())
print("\n\n Post learned Routes")
pprint(post_learn.to_dict())


