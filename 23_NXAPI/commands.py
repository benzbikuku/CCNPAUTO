e='''conf t
default int Eth1/2
int Eth1/2
description from-jsonrpc
aaa
no switch
ip address 15.15.15.15 255.255.255.0'''
print(e.replace('\n', ' ; '))