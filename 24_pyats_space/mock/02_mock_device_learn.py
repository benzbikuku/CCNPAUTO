

from pyats.topology import loader
tb = loader.load('mock.yaml')
dev = tb.devices['nx-osv-1']
dev.connect()

ospf_l = dev.learn('ospf')
print(dir(ospf_l))
print(ospf_l.to_dict())