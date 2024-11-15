
from pyats.topology import loader

tb = loader.load('/home/benz/CCNPAUTO/24_pyats_space/pyats/mock/my_testbed_test.yaml')
dev = tb.devices['CSR-173']


# print("TELNET CONNECTION")
# dev.connect(alias='ssh', via='cli', log_stdout=False)
# # print(dev.telnet.execute("show users"))

print("SSH CONNECTION")
dev.connect(alias='ssh', via='cli')
print(dev.ssh.execute("show version"))




