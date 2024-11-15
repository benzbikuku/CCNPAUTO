
from pyats.topology import loader
tb = loader.load('mock.yaml')
dev = tb.devices['nx-osv-1']
dev.connect()

p1 = dev.parse("show inventory")
print(p1)
print('My serial for slot1 is: ' + p1['name']['Slot 1']['serial_number'])