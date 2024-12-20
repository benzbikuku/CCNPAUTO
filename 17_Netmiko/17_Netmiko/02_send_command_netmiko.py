from netmiko import Netmiko

csr = {
    'device_type': 'cisco_ios',
    'host':   '192.168.1.149',
    'username': 'cisco',
    'password': 'cisco'
}
net_connect = Netmiko(**csr)
print("Connected successfully")

# cmd_output = net_connect.send_command("show ip int brief")
cmd_output = net_connect.send_command("ping 192.168.1.254 repeat 5", read_timeout=20, expect_string=r"ENT.+#")
print(cmd_output)
net_connect.disconnect()