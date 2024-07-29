import time
from paramiko import client
from getpass import getpass

# hostname = input("Enter the hostname: ")
username = input("Enter username: ")
if not username:
    username = 'admin'
print(f"The provided username is {username}")
# password = getpass(f"Enter password for {username}: ") or "admin"
csr_command = ['show run', 'sh version']
# nxsos_command = ['show version']


def exec_cmd_executor(hostname, cmd):
    password = getpass(f" \U0001F511 Enter password for {hostname}: ") or "admin"
    ssh_client = client.SSHClient()
    ssh_client.set_missing_host_key_policy(client.AutoAddPolicy)
    ssh_client.connect(hostname=hostname, username=username, port=22, password=password, look_for_keys=False,
                       allow_agent=False)
    print(f"successfully connected to device {hostname}")

    for command in cmd:
        print(f"\n{'#' * 10} Executing {command} {'#' * 10}")
        stdin, stdout, stderr = ssh_client.exec_command(command)
        # print(stdin.read().decode())
        print(stdout.read().decode())
        err = stderr.read().decode()
        if err:
            print(f"Error Occurred : {err}")


exec_cmd_executor("192.168.1.43", csr_command)

time.sleep(5)
# exec_cmd_executor("192.168.1.43",nxsos_command)
