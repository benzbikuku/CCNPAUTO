from netmiko import ConnectHandler

csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.149',
    'username': 'cisco',
    'password': 'cisco'
}
copy_cmd = "copy  csr1000v-mono-universalk9.16.04.01.SPA.pkg bootflash:new.pkg"
# copy_cmd_e = r"Destination filename"

cmd_list = [[copy_cmd, r".+#"]] 
            # copy_cmd_e],
            # ['\n', "Do you want to over write"],
            # ['\n', r'#']]

net_connect = ConnectHandler(**csr)
print("Connected successfully")

# cmd_output = net_connect.send_multiline(['show version', 'show ip int brief'])
cmd_output = net_connect.send_multiline(cmd_list, read_timeout=50)

print(cmd_output)
