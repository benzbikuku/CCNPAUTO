import sys
import time
import traceback

from paramiko import client,ssh_exception
from getpass import getpass

# hostname = input("Enter the hostname: ")
username = input("Enter username: ")
if not username:
    username = 'admin'
print(f"The provided username is {username}")
# password = getpass(f"Enter password for {username}: ") or "admin"
csr_command = ['conf t', ' int lo101', 'ip address 1.1.1.1 255.255.255.255', 'end', 'terminal len 0', 'show run']
nxsos_command = ['conf t', ' int lo101', 'ip address 1.1.1.1 255.255.255.255', 'end', 'terminal len 0', 'show run']


def cisco_cmd_executor(hostname, cmd):
    try:
        password = getpass(f"Enter password for {hostname}: ") or "admin"
        ssh_client = client.SSHClient()
        ssh_client.set_missing_host_key_policy(client.AutoAddPolicy)
        ssh_client.connect(hostname=hostname, username=username, port=22, password=password, look_for_keys=False,
                           allow_agent=False)
        print(f"successfully connected to device {hostname}")
        device_access = ssh_client.invoke_shell()

        for command in cmd:
            device_access.send(f'{command}\n')
            time.sleep(2)
            ouput = device_access.recv(65535)
            print(ouput.decode(), end='')
        # ssh_client.close()
    except ssh_exception.AuthenticationException:
        print("Check ssh credentials")
    except ssh_exception.NoValidConnectionsError:
        print("Please check connection to the router")
    except:
        print("Error found")
        print(sys.exc_info())
        traceback.print_exception(*sys.exc_info())


cisco_cmd_executor("192.168.1.15",csr_command)

time.sleep(5)
cisco_cmd_executor("192.168.1.16",nxsos_command)
# device_access.send("terminal len 0\n")
# device_access.send("show run\n")

# time.sleep(5)
# ouput = device_access.recv(65535)
# #print(ouput)
# print(ouput.decode())
# ssh_client.close()
# # print("Connected successfully")
