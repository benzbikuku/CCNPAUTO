import time

from paramiko import client
from getpass import getpass

hostname = '192.168.1.15'
username = input("Enter username: ")
if not username:
    username = 'admin'
print(f"The provided username is {username}")
password = getpass(f"Enter password for {username}: ") or "admin"
ssh_client = client.SSHClient()
ssh_client.set_missing_host_key_policy(client.AutoAddPolicy)
ssh_client.connect(hostname=hostname, username=username, port=22, password=password, look_for_keys=False,
                   allow_agent=False)
device_access = ssh_client.invoke_shell()
device_access.send("terminal len 0\n")
device_access.send("show run\n")

time.sleep(5)
ouput = device_access.recv(65535)
print(ouput)
# print(ouput.decode())
ssh_client.close()
# print("Connected successfully")
