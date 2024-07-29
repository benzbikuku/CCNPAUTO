import sys
import time
import traceback
import socket
import datetime
import paramiko.util
from paramiko import client,ssh_exception, RSAKey
from getpass import getpass
paramiko.util.log_to_file("paramiko.log", level="DEBUG")
# hostname = input("Enter the hostname: ")
username = input("Enter username: ")
if not username:
    username = 'admin'
print(f"The provided username is {username}")  
# password = getpass(f"Enter password for {username}: ") or "admin"
csr_command = ['conf t', ' int lo101', 'ip address 1.1.1.1 255.255.255.255', 'end', 'terminal len 0', 'show run']
# nxsos_command = ['conf t', ' int lo101', 'ip address 1.1.1.1 255.255.255.255', 'end', 'terminal len 0', 'show run']
key_file= RSAKey.from_private_key_file(filename="/home/benz/.ssh/id_rsa")
"""with open("/home/benz/ENTAUTO/CCNPAUTO/Files_Operations/config1.txt", 'r') as conf_file:
    csr_command = conf_file.readlines()
    # print(csr_command)
 """

def cisco_cmd_executor(hostname, cmd):
    try:
        # password = getpass(f"Enter password for {hostname}: ") or "admin"
        
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy)
        ssh_client.connect(hostname=hostname, username=username, port=22, look_for_keys=True,
                           allow_agent=True,
                           pkey=key_file,
                           disabled_algorithms=dict(pubkeys=['rsa-sha2-512', 'rsa-sha2-256']))
        print(f"successfully connected to device {hostname}")
        device_access = ssh_client.invoke_shell()
        now = datetime.datetime.now().replace(microsecond=0)
        current_config_file = f"{now}_{hostname}.txt"
        
        with open(current_config_file,'w') as output_data:

            for command in cmd:
                device_access.send(f'{command}')
                time.sleep(2)
                ouput = device_access.recv(65535)
                print(ouput.decode(), end='')
                output_data.write(ouput.decode())
            # ssh_client.close()
    except ssh_exception.AuthenticationException:
        print("Check ssh credentials")
    except ssh_exception.NoValidConnectionsError:
        print("Please check connection to the router")
    except:
        print("Error found")
        print(sys.exc_info())
        traceback.print_exception(*sys.exc_info())


cisco_cmd_executor("192.168.1.43",csr_command)

# time.sleep(5)
# cisco_cmd_executor("192.168.1.16",nxsos_command)
# device_access.send("terminal len 0\n")
# device_access.send("show run\n")

# time.sleep(5)
# ouput = device_access.recv(65535)
# #print(ouput)
# print(ouput.decode())
# ssh_client.close()
# # print("Connected successfully")
