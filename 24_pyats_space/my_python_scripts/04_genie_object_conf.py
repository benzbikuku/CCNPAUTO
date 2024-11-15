
from pyats.topology import loader
from genie.conf.base import Interface

tb = loader.load('/home/benz/CCNPAUTO/24_pyats_space/yaml/my_testbed_test.yaml')
dev = tb.devices['CSR-173']
dev.connect()

csr_int = Interface(device=dev, name="GigabitEthernet3")
print(type(csr_int))
print(dir(csr_int))

csr_int.ipv4 = '22.3.3.3'
csr_int.ipv4.netmask = '255.255.255.0'
csr_int.enable = True
# print(type(csr_int.ipv4))
# print(dir(csr_int.ipv4))

print(csr_int.build_config(apply=True))
