from netmiko import Netmiko

csr = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.149',
    'username': 'cisco',
    'password': 'cisco'
}
copy_cmd = 'copy bootflash:csr1000v-mono-universalk9.16.04.01.SPA.pkg bootflash:new.pkg'
net_connect = Netmiko(**csr)
print("Connected successfully")

run_df = net_connect.send_command(copy_cmd, read_timeout=100, expect_string=".+#")
print(run_df)
# run_ov = net_connect.send_command("\n") #, expect_string="Do you want to over write")
# print(run_ov)
# run_c = net_connect.send_command("\n", expect_string=".+#", read_timeout=50)
# print(run_c)
net_connect.disconnect()


