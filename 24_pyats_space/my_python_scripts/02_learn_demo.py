
from pyats.topology import loader
tb = loader.load('/home/benz/CCNPAUTO/24_pyats_space/yaml/my_testbed_test.yaml')
dev = tb.devices['CSR-173']
dev.connect(log_stdout=False, learn_hostname=True)

# learn_int = dev.learn("interface")
# print(learn_int.to_dict())

# learn_route = dev.learn("static_routing")
# print(learn_route.to_dict())

learn_ospf = dev.learn("ospf")
print(learn_ospf.to_dict())