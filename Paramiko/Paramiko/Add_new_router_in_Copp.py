import datetime
from deviceconfig import cisco_cmd_executor
interfaces = []
router_number = input("Please define the Copp Router number. A one digit number as 1 or 2: " )
hostname= f"Copp_R{str(router_number)}.ant.amazon.com"
print(hostname)
router_interface = input("Please Enter the router  interface that connects to the core router, For example[GigabitEthernet1]: ")
wan_interface = input ("Please Enter the core router interface that connects to this router being added1, For example[GigabitEthernet1]: ")
# now = datetime.datetime.now().replace(microsecond=0)
config_file_name = f"{hostname}_config_file"
# print(config_file_name)

print(f"{'#'*10} Configure router interfaces {'#'*10}")  

print(f"{'#'*5} Configure router interface that connect to the core router {'#'*5}")  



router_interface_name = f" int {router_interface}\n"
interfaces.append(router_interface_name)
router_interface_ip = f"ip address 10.10.1{router_number}.{router_number} 255.255.255.0\n"
interfaces.append(router_interface_ip)
router_no_shut = "no shutdown\n"
interfaces.append(router_no_shut)




print(f"{'#'*5} Configure core interface that connect to the router being added {'#'*5}") 

wan_interface_name = f" int {wan_interface}\n"
# interfaces.append(wan_interface_name)
wan_interface_ip = f"ip address 10.10.1{router_number}.1 255.255.255.0\n"
# interfaces.append(wan_interface_ip)
wan_no_shut = "no shutdown\n"
# interfaces.append(wan_no_shut)

print(f"{'#'*5} Configure interface Loopback 0 {'#'*5}") 

int_loop_0 = "int lo 0\n"
interfaces.append(int_loop_0)
Lo_interface_ip = f"ip address 10.10.{router_number}.{router_number} 255.255.255.255 \n"
interfaces.append(Lo_interface_ip)
Lo_no_shut = "no shutdown\n"
interfaces.append(Lo_no_shut)

print(f"{'#'*5} Configure interface Loopback 1 {'#'*5}") 

int_loop_1 = "int lo 1\n"
interfaces.append(int_loop_1)
L1_interface_ip = f"ip address 172.6.{router_number}.{router_number} 255.255.255.255\n"
interfaces.append(L1_interface_ip)
L1_no_shut = "no shutdown\n"
interfaces.append(L1_no_shut)


with open('/home/benz/ENTAUTO/CCNPAUTO/Paramiko/Paramiko/Copp_router_template', 'r') as Copp_router_template:
    template = Copp_router_template.readlines()
# print(template)

updated_config = template + interfaces

# print(updated_config)
with open(config_file_name,'w') as config_data:
    for cmd in updated_config:
        config_data.write(cmd)
        # print(cmd)
print(config_file_name)
with open(config_file_name,'r') as commands:
    command_lines= commands.readlines()
    
# print(command_lines)
cisco_cmd_executor("192.168.1.19", command_lines)
    

