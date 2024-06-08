from netmiko import Netmiko
my_router = Netmiko(ip='192.168.1.15', username='cisco', password='cisco',
                    device_type='cisco_ios')
# print(my_router.find_prompt())
show_run=my_router.send_command('show run')
print(show_run)